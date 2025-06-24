import inspect
import base64
import requests

def call_with_filtered_kwargs(func, **kwargs):
    sig = inspect.signature(func)
    params = sig.parameters
    filtered_kwargs ={k:v for k, v in kwargs.items() if k in params}
    return func(**filtered_kwargs)


def image_url_to_base64(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    image_bytes = response.content
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    return image_base64