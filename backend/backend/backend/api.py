from ninja import NinjaAPI
from sources.api import router as sources_router
from sources.models import Source

api = NinjaAPI()
api.add_router("/sources", sources_router)


@api.get("/status")
def status(request):
    return {
        "sources": False,
        "profiling": not bool(len(Source.objects.all())),
        "cleaning": True,
        "deploy": True,
    }
