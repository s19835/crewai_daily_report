import os

def get_api_key(key_name):
    api_key = os.environ.get(key_name)
    if api_key is None:
        raise ValueError(f"{key_name} envronment variable is not set")
    return api_key