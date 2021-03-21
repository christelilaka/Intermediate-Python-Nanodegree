from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """Ingestor of .docx files"""
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Returns a list of Quotes
        Arguments:
            path {str} -- path of the docx file.
        Raises:
            Exceptions: if file extensin is not docx.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception. Check the file extension.')

        quotes = []
        doc = docx.Document(path)

        for line in doc.paragraphs:
            if line.text != '':
                parse = line.text.split('-')
                new_quote = QuoteModel(parse[0].replace('"', '').strip(), parse[1].replace('"', '').strip())
                quotes.append(new_quote)

        return quotes