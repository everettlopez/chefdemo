from fastapi import APIRouter

from app.api.routes import health_routes, item_routes, test_routes

api_router = APIRouter(prefix="/api")
api_router.include_router(test_routes.router)
api_router.include_router(item_routes.router)

root_router = APIRouter()
root_router.include_router(health_routes.router)
root_router.include_router(api_router)
