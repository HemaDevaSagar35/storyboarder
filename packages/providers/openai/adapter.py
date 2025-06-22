import base64
from openai import OpenAI
from ..base import ImageProvider
from ..registry import register


@register
class OpenAIAdapter(ImageProvider):
    name = "OpenAI (gpt-image-1)"
    slug = "openai"

    async def generate_image(self, prompt: str, **kwargs):
        #TODO: for now the output is a base64 encoded bytes. How does this get returned to the user?
        #create the client initiation here itself and remove __init__
        client = OpenAI(api_key=kwargs.get("api_key"))
        response = client.images.generate(
            model = "gpt-image-1",
            prompt=prompt)
        
        image_base64 = response.data[0].b64_json
        #image_bytes = base64.b64decode(image_base64)
        return f"data:image/png;base64,{image_base64}"