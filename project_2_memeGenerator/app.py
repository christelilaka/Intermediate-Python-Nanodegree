import random
import os
import requests
from flask import Flask, render_template, abort, request
import urllib.request as url_request
from PIL import Image

from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    _, _, paths = next(os.walk(images_path))
    imgs = [f'{images_path}{path}' for path in paths]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    print(path)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    tem_img = './tem_image.jpg'

    req = url_request.urlopen(url)
    with open(tem_img, 'wb') as img_file:
        img_file.write(req.read())

    path = meme.make_meme(tem_img, body, author)
    os.remove(tem_img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
