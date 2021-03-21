# The Meme Generator App
The `meme generator` is a multimedia application that dynamically generates memes, including an image with an overlaid quote. Quotes are saved in a variety of filtetypes (.pdf, .docx, .txt, .csv). The application selects a random quote and overlais it on a random image.

This application has two main modules:
- The `Quote Engine` module is responsible for ingesting many types of files that contain quotes. A _quote_ contains a _body_ and an _author_:
```"This is a quote body" - Author```
- The `Meme Engine` module is responsible for manipulating and drawing text onto images. 
can be run on the web or in the command line.

## How to run the program 

The `requirements.txt` file has all the modules and dependencies need to run this application.
Run the following command to install all the requierements.

```shell
$ pip install -r requirements.txt
```

The [pdftotext](https://www.xpdfreader.com/pdftotext-man.html) converter must also be installed on the server running the application.

#### Running the application in the command line

The project conains a `meme.py` filte that can be executed in the command line. This program takes tree optional artuments:
- `--path`: An image path
- `--body`: A string quote body
- `--author`: A string quote author

Here's an example of a command:

```shell
$ python3 meme.py --path="./_data/photos/dog/xander_1.jpg" --body="La vie est belle!" --author="Ilaka"
```

The program returns a path to a generated image. _if any argument is not defined, a random selection is used._

#### Running the application on the web

The run the application on the web we'll have to start a Flask server by running the following command:

```shell
$ flask run --host 0.0.0.0 --port 3000 --reload
```

You can change the `host` and `port` here.
Once the server is up and running, we can navigate to http://0.0.0.0:3000/ to interact with the web interface.

## Roles-and-responsabilities of all sub-modules

### Quote Engine Module

This module has the following sub-modules:
- **QuoteMode** class: defines a `QuoteMode` object, which contains text fields for body and author.
- **IngestorInterface** class: an abstract base class which defines a complete `classmethod` method to verify if the file type is compatible with the ingestor class, and an abstract method for parsing the file content and outputting it to a `QuoteMode` object.

The following classes inherits from the `IngestorInterface` class and return a valid `QuoteModel`:

- The **TextIngestor** class does not depend on any 3rd party library to complete the defined, abstract method signatures to parse **Text** files.
- The **DocxIngestor** class depends on the `python-docx` library to complete the defined, abstract method signatures to parse **DOCX** files.
- The **PDFIngestor** class utilizes the `subprocess` module to call the [pdftotext](https://www.xpdfreader.com/pdftotext-man.html) CLI utility—creating a pipeline that converts PDFs to text and then ingests the text. The class handles deleting temporary files.
- The **CSVIngestor** class depends on the `pandas` library to complete the defined, abstract method signatures to parse CSV files.

All ingestors are packaged into a main `Ingestor` class which encapsulates all the ingestors to provide one interface to load any supported file type.

We can importe this module like:

```python
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel

# Example
quotes = Ingestor.parse('file_path')
```

### Meme Generator Module

This module has the following responsabilities:
- Loading of a file from disk
- Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
- Add a caption to an image (string input) with a body and author to a random location on the image.

The class depends on the `Pillow` library to complete the defined, incomplete method signatures so that they work with JPEG/PNG files.

```python
from MemeEngine import MemeEngine

# Example
meme = MemeEngine('path_to_a_folder_where_image_will_be_saved')
path = meme.make_meme(img, quote_body, quote_author)   
```