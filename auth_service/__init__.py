from fastapi import FastAPI

from .routers.router import router_identification
from .client import client, port


app = FastAPI()
app.include_router(router_identification)
