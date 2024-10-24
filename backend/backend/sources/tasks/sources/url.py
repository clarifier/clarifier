from django_rq import job
from rq.job import Retry

from sources.models import Source
from backend.utils import clickhouse


@job("sources", retry=Retry(max=5, interval=30))
def download_url_source(source: Source, url: str):
    # Connect to ClickHouse
    client = clickhouse()
    source.data["status"] = "fetching"
    source.save()
    # Pull into ClickHouse
    try:
        client.command(f"""
            CREATE TABLE source_pk_{source.pk}
            ENGINE = MergeTree
            ORDER BY tuple()
            AS FROM url('{url}', Parquet) SELECT *;""")
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
    "download_url_source",
]
