import os, sys
import random
from PIL import Image

stegoboi = Image.open("./stegosaurus.png")
width, height = stegoboi.size

key = [random.randint(0,1) for x in range(width * height)]

keypic = Image.new('1', (width, height))
keypic.putdata(key)
keypic.save("key.bmp")

if (__name__ == "__main__"):
    print(key)