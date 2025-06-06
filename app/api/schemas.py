from typing import Optional

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    longitude: float = Field(..., ge=-180.0, le=180.0)
    latitude: float = Field(..., ge=-90.0, le=90.0)


class ItemResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    longitude: float
    latitude: float
