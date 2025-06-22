from providers.registry import get_provider


class ImageGeneratorService:
    async def generate_image(self, *, prompt: str, provider_slug: str, **params):
        try:
            provider_class = get_provider(provider_slug)
            provider = provider_class()
            output = await provider.generate_image(prompt, **params)

            return {"image": output}
        except Exception as e:
            return {"error": str(e)}

image_generator_service = ImageGeneratorService()