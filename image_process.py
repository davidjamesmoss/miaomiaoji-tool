#!/usr/bin/python
# -*-coding:utf-8-*-

from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps


class ImageConverter:
    @staticmethod
    def image2bmp(path):
        img = Image.open(path)
        img.thumbnail((384, 9999), Image.ANTIALIAS)  # Reduce to fit and maintain aspect ratio.
        img = PIL.ImageOps.invert(img)  # Invert image for printing
        img = img.convert('1')  # Convert to 1-bit with dither
        return img.tobytes()


class TextConverter:
    @staticmethod
    def text2bmp(text, font_path, font_size=40):
        img = Image.new('1', (384, 100), 0)  # Black background
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, font_size)
        draw.text((0, 0), text, 1, font=font)  # White text
        return img.tobytes()
