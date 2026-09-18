"""Health and readiness endpoints."""

from fastapi import APIRouter

from api.schemas import HealthResponse
from core.config import get_settings

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse, summary="Check service health")
def health_check() -> HealthResponse:
    """Return process-level health before infrastructure dependencies are introduced."""

    settings = get_settings()
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        environment=settings.environment,
    )