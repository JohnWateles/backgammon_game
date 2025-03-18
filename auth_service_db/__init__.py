from fastapi import FastAPI

from .routers.router import router, router_get_only_messages
from .client import client, port


app = FastAPI()
app.include_router(router)
app.include_router(router_get_only_messages)
