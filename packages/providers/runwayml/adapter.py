import base64
from providers.base import ImageProvider
from providers.registry import register
from runwayml import RunwayML
from shared.utils import call_with_filtered_kwargs, imae_url_to_base64

@register
class RunwayMLAdapter(ImageProvider):
    name = "RunwayML"
    slug = "runwayml"

    async def generate_image(self, prompt: str, **kwargs):
        try:
            client = RunwayML(api_key=kwargs.get("api_key"))
            params = {"model": "gen4_image", "prompt_text":prompt, **kwargs}
            response = call_with_filtered_kwargs(client.text_to_image.create, **params)

            output = response.wait_for_task_output()
            url = output.output[0]
            image_base64 = imae_url_to_base64(url)
            return f"data:image/png;base64,{image_base64}"
            
        except Exception as e:
            raise e
        
