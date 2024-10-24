from django_rq import job
from rq.job import Retry

from sources.models import Source
from backend.utils import clickhouse
import requests


@job("sources", retry=Retry(max=5, interval=30))
def download_openml_source(source: Source, id: str):
    # Connect to ClickHouse
    client = clickhouse()
    source.data["status"] = "working"
    source.save()
    # Get data from OpenML
    res = requests.get(f"https://www.openml.org/api/v1/json/data/{id}")
    if res.status_code != 200:
        source.data["status"] = "error"
        source.data["error"] = "failed to fetch metadata from OpenML"
        source.save()
        return
    data = res.json().get("data_set_description")
    source.data["status"] = "fetching"
    source.data["url"] = data.get("parquet_url")
    source.name = data.get("name")
    source.description = data.get("description")
    source.save()
    # Fail if no parquet file
    if not data.get("parquet_url"):
        source.data["status"] = "failed"
        source.data["error"] = "no parquet available"
        source.save()
        return
    # Pull into ClickHouse
    try:
        client.command(f"""
            CREATE TABLE source_pk_{source.pk}
            ENGINE = MergeTree
            ORDER BY tuple()
            AS FROM url('{data.get("parquet_url")}', Parquet) SELECT *;""")
        source.data["status"] = "success"
        source.data["ch_table"] = f"source_pk_{source.pk}"
        source.save()
        return
    except Exception as e:
        source.data["status"] = "failed"
        source.data["error"] = str(e)
        source.save()
        return


__all__ = [
    "download_openml_source",
]
