from app.src.app import app
import logging
from concurrent.futures.thread import ThreadPoolExecutor

from app.src.common.app import app
from starlette.middleware.cors import CORSMiddleware
from starlette_prometheus import PrometheusMiddleware

from app.src.controller.repo_controller import repo_manager_router
from app.src.controller.priority_controller import priority_manager_router
from app.src.controller.msg_controller import msg_manager_router

from decouple import config

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(PrometheusMiddleware)

app.include_router(repo_manager_router, tags=['Repo'], prefix=config("PREFIX_API"))
app.include_router(priority_manager_router, tags=['Priority'], prefix=config("PREFIX_API"))
app.include_router(msg_manager_router, tags=['Message'], prefix=config("PREFIX_API"))