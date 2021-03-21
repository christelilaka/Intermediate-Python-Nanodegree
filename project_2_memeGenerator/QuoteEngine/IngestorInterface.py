from abc import ABC, abstractclassmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Test if extension can be ingested"""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

@classmethod
@abstractclassmethod
def parse(cls, path: str) -> List[QuoteModel]:
    pass