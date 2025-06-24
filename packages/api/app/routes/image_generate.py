import os
from fastapi import APIRouter
from shared.data import ImageGenRequest, ImageGenResponse
from api.app.services.image_generator import image_generator_service



router = APIRouter()
@router.post("/image/generate", response_model=ImageGenResponse)
async def generate_image(request: ImageGenRequest):
    prompt = request.prompt
    provider = request.provider
    params = request.params

    params["api_key"] = os.getenv(f"{provider.upper()}_API_KEY")
    response = await image_generator_service.generate_image(prompt=prompt, provider_slug=provider, **params)

    return ImageGenResponse(image=response.get("image", ""), image_url = response.get("image_url", ""), error=response.get("error", None))