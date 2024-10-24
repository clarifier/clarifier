from typing import Any, List, Optional

from ninja import File, Form, Router, UploadedFile
from ninja.errors import HttpError
from ninja.pagination import paginate
from django.db import transaction
from django.shortcuts import get_object_or_404
from datetime import datetime

from backend.utils import clickhouse
from sources.api.schemas import (
    SourceSchema,
    SourceFromFile,
    SourceFromURL,
    SourceFromOpenML,
    SourceFromKaggle,
    SourceFromTFDS,
)
from sources.models import Source
from sources.tasks import download_openml_source

from clickhouse_connect.driver.exceptions import DatabaseError

from sources.tasks.sources.url import download_url_source

router = Router(tags=["sources"])


@router.get("/", response=List[SourceSchema])
@paginate
def list_sources(request):
    return Source.objects.all()


@router.get("/{id}/", response=SourceSchema)
def get_source(request, id: str):
    return get_object_or_404(Source, pk=id)


@router.post("/upload/file", response=SourceSchema)
def upload_source_by_file(
    request,
    details: Form[SourceFromFile],
    file: File[UploadedFile],
):
    pass


@router.post("/upload/url", response=SourceSchema)
def upload_source_by_url(request, details: SourceFromURL):
    source = Source.objects.create(
        name=details.name,
        description=details.description,
        size="",
        source="url",
        data={"status": "queued"},
    )
    download_url_source.delay(source, details.url)
    return {"pk": source.pk}


@router.post("/upload/openml", response=SourceSchema)
def upload_source_by_openml_id(request, details: SourceFromOpenML):
    source = Source.objects.create(
        name="",
        description="",
        size="",
        source="openml",
        data={
            "id": details.id,
            "status": "queued",
        },
    )
    download_openml_source.delay(source, details.id)
    return {"pk": source.pk}


@router.post("/upload/kaggle", response=SourceSchema, include_in_schema=False)
def upload_source_by_kaggle_id(request, details: SourceFromKaggle):
    raise HttpError(412, "This feature is not ready yet")
    pass


@router.post("/upload/tfds", response=SourceSchema, include_in_schema=False)
def upload_source_by_tfds_id(request, details: SourceFromTFDS):
    raise HttpError(412, "This feature is not ready yet")
    pass
