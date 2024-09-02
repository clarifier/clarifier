from typing import Any, List, Optional

from ninja import Router
from ninja.errors import HttpError
from ninja.pagination import paginate
from django.db import transaction
from django.shortcuts import get_object_or_404
from datetime import datetime

router = Router(tags=["sources"])


@router.get("/", response=List[Any])
@paginate
def list_sources(request):
    return []


@router.get("/{id}/", response=Any)
def get_source(request, id: str):
    return "hello"
