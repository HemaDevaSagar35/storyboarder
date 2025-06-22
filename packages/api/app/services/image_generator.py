from providers.registry import get_provider


class ImageGeneratorService:
    async def generate_image(self, *, prompt: str, provider_slug: str, **params):
        provider_class = get_provider(provider_slug)
        provider = provider_class()
        output = await provider.generate_image(prompt, **params)

        return output

image_generator_service = ImageGeneratorService()