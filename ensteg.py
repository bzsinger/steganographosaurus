import os, sys
from PIL import Image

def tobits(msg):
    return [bin(i)[2:] for i in bytearray(msg, 'ascii')]

def write_stego(key, bin_list, filename):
    bit_place = 0
    stegoboi = Image.open(filename)
    stego2boi = stegoboi.copy()
    #Go through each pixel, and if the pixel is off in the key, place a bit
    #in the last part of the pixel
    for x in range(height):
        for y in range(width): 
            if key[y + x*width] == 0 and bit_place < len(bin_list):            
                pixelO = stego2boi.getpixel((x,y))
                pixelO = tuple([((i >> 1) << 1) + int(bin_list[bit_place]) for i in pixelO])
                bit_place +=1
                stego2boi.putpixel((x,y), pixelO) 
    stego2boi.save("stego2.bmp")

