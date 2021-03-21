"""The Quote Engine module is responsible for ingesting many types of files that contain quotes.
    This module uses the docx, csv, txt, and pdf ingestor to ingest files."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor

class Ingestor(IngestorInterface):
    """Select the appropriate helper for a given file, based on filetype."""
    ingestors = [DocxIngestor, CSVIngestor, TXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)