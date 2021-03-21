import pandas
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Ingestor of .csv files"""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Returns a list of Quotes
        Arguments:
            path {str} -- path of the csv file
        Raises:
            Exceptions: if file extensin is not csv
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest extension.')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
