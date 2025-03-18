from fastapi import FastAPI

from .routers.router import router
from .client import client, port

app = FastAPI()
app.include_router(router)
