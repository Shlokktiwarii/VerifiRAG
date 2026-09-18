from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Minimal health response used by local and container checks."""

    status: str = Field(description="Service health status.")
    service: str = Field(description="Logical application name.")
    environment: str = Field(description="Active runtime environment.")