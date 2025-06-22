from enum import Enum
from typing import Optional
from pydantic import BaseModel


class ImageGenRequest(BaseModel):
    prompt: str
    provider: str
    params: dict = {}


class ImageGenResponse(BaseModel):
    image: Optional[str] = ""
    error: Optional[str] = ""
