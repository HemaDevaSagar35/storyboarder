from abc import ABC, abstractmethod


class ImageProvider(ABC):
    name: str
    slug : str

    @abstractmethod
    async def generate_image(self, prompt: str, **kwargs):
        pass