from enum import Enum
from pydantic import BaseModel


class ImageGenRequest(BaseModel):
    prompt: str
    provider: str
    params: dict = {}


class ImageGenResponse(BaseModel):
    image: str

