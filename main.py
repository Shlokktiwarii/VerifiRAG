from fastapi import FastAPI

from api.routes_health import router as health_router
from core.config import get_settings


def create_app() -> FastAPI:
    """Create the HTTP application and register routes."""

    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="Evidence-first RAG over SEC financial filings.",
    )
    app.include_router(health_router)
    return app


app = create_app()