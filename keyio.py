import random
from PIL import Image

def generate_key(filename, message, keyname="key.bmp"):
    stegoboi = Image.open(filename)
    width, height = stegoboi.size
    length = len(message) * 8
    key_indices = random.sample(range(width * height), length)

    key = [0 for i in range(width * height)]
    for i in key_indices:
        key[i] = 1
    keypic = Image.new('1', (width, height))
    keypic.putdata(key)
    keypic.save(keyname)

def read_key(keyname="key.bmp"):
    keypic = Image.open(keyname)
    return [i%2 for i in list(keypic.getdata())]

