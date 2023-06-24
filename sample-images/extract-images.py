#!/usr/bin/env python

import sys

import numpy
from PIL import Image

if len(sys.argv) < 2:
    sys.exit("Usage: extract-images.py <filename>")

img = Image.open(sys.argv[1]).convert("L")
pixels = numpy.array(img)
tileWidth = 28
tileHeight = 28

# Flip from black on white to white on black
pixels = 255 - pixels

# Create the array of tiles (each width
tiles = [
    pixels[row : row + tileHeight, col : col + tileWidth]
    for row in range(0, pixels.shape[0], tileHeight)
    for col in range(0, pixels.shape[1], tileWidth)
]

num_digits = int(pixels.shape[0]/tileHeight)
num_examples = int(pixels.shape[1]/tileWidth)

for digit in range(0, num_digits):
    for example in range(0, num_examples):
        digit_image = Image.new('L', (tileWidth, tileHeight))
        digit_image.putdata(tiles[digit * num_examples + example].flatten())
        digit_image.save(f"sample-digit{digit}-example{example}.png")

