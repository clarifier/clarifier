from ninja import NinjaAPI
from sources.api import router as sources_router


api = NinjaAPI()
api.add_router("/sources", sources_router)
