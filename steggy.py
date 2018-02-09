import os, sys
import random
from PIL import Image

stegoboi = Image.open("./stegosaurus.png")
width, height = stegoboi.size
#random.randint(0,1)
key = [[(255,255,255) for x in range(width)] for y in range(height)]

keypic = Image.new('RGB', (width, height), "red")
keypic.putdata(key)
keypic.save("key.bmp")

if (__name__ == "__main__"):
    print(key)