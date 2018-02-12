import random
from PIL import Image

def generate_key(image, message, filename="key.bmp"):
    width, height = image.size
    length = len(message) * 8
    key_indices = random.sample(range(width * height), length)

    key = [0 for i in range(width * height)]
    for i in key_indices:
        key[i] = 1
    keypic = Image.new('1', (width, height))
    keypic.putdata(key)
    keypic.save(filename)

def read_key(filename="key.bmp"):
    keypic = Image.open(filename)
    return [i%2 for i in list(keypic.getdata())]