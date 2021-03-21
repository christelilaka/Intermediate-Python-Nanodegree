import os
import subprocess
from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class PDFIngestor(IngestorInterface):
    """Ingestor of .pdf files"""
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Returns a list of Quotes
        Arguments:
            path {str} -- path of the pdf file.
        Raises:
            Exceptions: if file extensin is not pdf.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception. Check the file extension.')

        temp_name = './pdf_converted.txt'

        pdf = subprocess.call(['pdftotext', path, temp_name])

        quotes = []

        with open(temp_name, 'r') as in_file:
            lines = in_file.readline().split(' "')
            for line in lines:
                line = line.strip('\n\r').strip()
                line = line.split('-')
                new_quote = QuoteModel(line[0].replace('"', '').strip(), line[1].replace('"', '').strip())
                quotes.append(new_quote)

        os.remove(temp_name)
        return quotes
