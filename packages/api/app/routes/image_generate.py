from fastapi import APIRouter
from shared.data import ImageGenRequest, ImageGenResponse
from services.image_generator import image_generator_service



router = APIRouter()
@router.post("/image/generate", response_model=ImageGenResponse)
async def generate_image(request: ImageGenRequest):
    prompt = request.prompt
    provider = request.provider
    params = request.params

    image = await image_generator_service.generate_image(prompt=prompt, provider_slug=provider, **params)
    return ImageGenResponse(image=image)