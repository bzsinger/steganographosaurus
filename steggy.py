import os, sys
import random
from PIL import Image

stegoboi = Image.open("./stegosaurus.png")
stego2boi = stegoboi.copy()
width, height = stegoboi.size

key = [random.randint(0,1) for x in range(width * height)]

keypic = Image.new('1', (width, height))
keypic.putdata(key)
keypic.save("key.bmp")

msg = "Hello World!"
def tobits(msg):
    return [bin(i)[2:] for i in bytearray(msg, 'ascii')]

#Need to cite 
def frombits(bin_list):
    return ''.join([chr(int(x, 2)) for x in bin_list])
"""
pseudocode:
    For every (x, y) flattened pixel, we check if keypic is true
    If so, the last two bits of every color of (x, y) will be modified

    getpixel(x, y)
    putpixel(x, y)
"""
def write_stego(bin_list):
    bit_place = 0
    for x in range(height):
        for y in range(width): 
            if key[y + x*width] == 1 and bit_place < len(bin_list):            
                pixelO = stego2boi.getpixel((x,y))
                pixelO = tuple([((i >> 1) << 1) + int(bin_list[bit_place]) for i in pixelO])
                bit_place +=1
                stego2boi.putpixel((x,y), pixelO) 
    stego2boi.save("stego2.bmp")

if (__name__ == "__main__"):
    print tobits(msg)
    result = tobits(msg)
    print frombits(result)  
    write_stego(result)

