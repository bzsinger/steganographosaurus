import os, sys
import random
from PIL import Image

stegoboi = Image.open("./stegosaurus.png")
width, height = stegoboi.size

key = [random.randint(0,1) for x in range(width * height)]

keypic = Image.new('1', (width, height))
keypic.putdata(key)
keypic.save("key.bmp")

msg = "Hello World!"
def tobits(msg):
    arr = bytearray(msg, 'ascii')
    results = []
    for i in arr:
        results.append(bin(i)[2:])
    return results


if (__name__ == "__main__"):

    print tobits(msg)
    #print(key)
