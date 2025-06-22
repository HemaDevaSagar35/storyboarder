import inspect


def call_with_filtered_kwargs(func, **kwargs):
    sig = inspect.signature(func)
    params = sig.parameters
    filtered_kwargs ={k:v for k, v in kwargs.items() if k in params}
    return func(**filtered_kwargs)