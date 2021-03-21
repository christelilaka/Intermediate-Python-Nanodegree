from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    """Ingestor of .txt files"""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Returns a list of Quotes
        Arguments:
            path {str} -- path of the .txt file.
        Raises:
            Exceptions: if file extensin is not txt.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception. Check the file extension.')

        quotes = []

        with open(path, 'r') as in_file:
            in_file = in_file.read()
            lines = in_file.split('\n')
            for line in lines:
                line = line.strip('\n\r').strip()
                line = line.split('-')
                if len(line) == 2:
                    new_quote = QuoteModel(line[0], line[1])
                    quotes.append(new_quote)

        return quotes