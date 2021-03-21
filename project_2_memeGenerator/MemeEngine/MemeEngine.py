"""Meme Engine: responsible for manipulating and drawing text onto images."""

from PIL import Image, ImageDraw, ImageFont
import os
import glob
import random
import string

class MemeEngine():
    def __init__(self, out_path):
        """Instantiate a MemeEngine object."""
        self.out_path = out_path

    def make_meme(self, img_path:str, text:str, quote_author:str, width=500) -> str:
        """Returns path of the resized image with quote and author drawn onto it.

        Arguments:
            img_path {str} -- path of the source image
            text {str} -- text body of the quote
            quote_author {str} -- author name.
            """
        img = Image.open(img_path)

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))

        img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)

        text_postition = [(20, 50), (50, 300), (100, 420)]
        position_body = random.choice(text_postition)
        position_author = (position_body[0]+50, position_body[1]+25)

        fnt = ImageFont.truetype("./fonts/NotoSans-Bold.ttf", 20)
        draw.text(position_body, text, fill='white', font=fnt, stroke_width=1, stroke_fill='black')
        draw.text(position_author, f'- {quote_author}', fill='white', font=fnt, stroke_width=1, stroke_fill='red')
        
        letters = string.ascii_lowercase
        out_name = ''.join(random.choice(letters) for i in range(5)) + '.jpg'

        try:
            os.mkdir(self.out_path)
        except:
            files = glob.glob(f'{self.out_path}/*.jpg')
            if len(files) !=0:
                for f in files:
                    os.remove(f)
        finally:
            img.save(f'{self.out_path}/{out_name}')

        return f'{self.out_path}/{out_name}'