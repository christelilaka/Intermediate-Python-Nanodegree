class QuoteModel():
    """Create a Quote object 
    """
    def __init__(self, body:str, author:str):
        """Instantiates the Quote object
        Arguments:
            body {str} -- the body of the quote
            author {str} -- the name of the author
        """
        self.body = body
        self.author = author

    def __str__(self):
        return f'"{self.body}" - {self.author}'

    def __repr__(self):
        return f'QuoteModel(body="{self.body}", author="{self.author}")'