import os, sys
import random
from PIL import Image

stegoboi = Image.open("./stegosaurus.png")
width, height = stegoboi.size


def generate_key(filename="key.bmp"):
    key = [random.randint(0,1) for x in range(width * height)]
    keypic = Image.new('1', (width, height))
    keypic.putdata(key)
    keypic.save(filename)

def read_key(filename="key.bmp"):
    keypic = Image.open(filename)
    return [i%2 for i in list(keypic.getdata())]


msg = "Hello World!"
def tobits(msg):
    return [bin(i)[2:] for i in bytearray(msg, 'ascii')]

#Need to cite 
def frombits(bin_list):
    return ''.join([chr(int(x, 2)) for x in bin_list])


if (__name__ == "__main__"):
    generate_key()

    print(read_key())

    # print(tobits(msg))
    # result = tobits(msg)
    # print(frombits(result)) 
