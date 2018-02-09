import os, sys
from PIL import Image

stegoboi = Image.open("./stegosaurus.png")


if (__name__ == "__main__"):
    print(stegoboi.size)