from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.healthcheck import router as healthcheck_router

API_VERSION = "v1"

tags_metadata = [
    {"name": "Healthcheck"},
    {"name": "Auth"},
    {"name": "Transaction Request Analyser"},
    {"name": "Transaction Request Checked  Webhook "},
]


def create_app() -> FastAPI:
    app = FastAPI(
        title="Core API Anti Fraud",
        description="Service build stack python responsible for encapsulating fraud engine rules",
        version=API_VERSION,
        openapi_tags=tags_metadata,
        root_path="",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.router.redirect_slashes = True

    app.include_router(
        healthcheck_router, prefix=f"/{API_VERSION}", tags=["Healthcheck"]
    )

    return app
