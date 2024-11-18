from typing import List
from workspace.models import Workspace
from ninja import Router, ModelSchema
from ninja.pagination import paginate


class WorkspaceSchema(ModelSchema):
    class Meta:
        model = Workspace
        fields = "__all__"


router = Router(tags=["workspace"])


@router.get("/", response=List[WorkspaceSchema])
@paginate
def list_workspaces(request):
    return Workspace.objects.all()


__all__ = ["router"]
