from typing import Dict, Type, List
from .base import ImageProvider

_registry: Dict[str, Type[ImageProvider]] = {}

def register(cls: Type[ImageProvider]) -> Type[ImageProvider]:
    slug = getattr(cls, "slug", cls.__name__.lower())
    if slug in _registry:
        raise ValueError(f"Provider with {slug} already registered")
    _registry[slug] = cls
    return cls

def get_provider(slug: str) -> Type[ImageProvider]:
    if slug not in _registry:
        raise ValueError(f"No provider {slug} registered.\n Available providers: {list_providers()}")
    return _registry[slug]

def list_providers() -> List[Type[ImageProvider]]:
    return list(_registry.values())