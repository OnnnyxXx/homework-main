from typing import Type

from storage import JSONStorage, Storage
from tasks.storage import JSONStorage


def get_storage() -> JSONStorage:
    """
       Return a Storage object by creating and returning a new instance of JSONStorage.
    """
    return JSONStorage(file_path='data.json')
