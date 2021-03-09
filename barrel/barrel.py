import fastapi

from .routers import resources

app = fastapi.FastAPI()

app.include_router(resources.router)