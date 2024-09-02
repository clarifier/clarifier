from typing import Any, List, Optional

from ninja import File, Form, Router, UploadedFile
from ninja.errors import HttpError
from ninja.pagination import paginate
from django.db import transaction
from django.shortcuts import get_object_or_404
from datetime import datetime

from sources.api.schemas import (
    SourceSchema,
    SourceFromFile,
    SourceFromURL,
    SourceFromOpenML,
    SourceFromTFDS,
)
from sources.models import Source

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
    pass


@router.post("/upload/openml", response=SourceSchema)
def upload_source_by_openml_id(request, details: SourceFromOpenML):
    pass


@router.post("/upload/tfds", response=SourceSchema)
def upload_source_by_tfds_id(request, details: SourceFromTFDS):
    pass
