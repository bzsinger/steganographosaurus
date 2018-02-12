import os, sys
from PIL import Image

def tobits(message):
    return "".join(["{:08b}".format(i) for i in bytearray(message, 'ascii')])

def write_stego(key, message, filename, output = "stego.bmp"):
    bit_place = 0
    bin_string = tobits(message)
    stegoboi = Image.open(filename)
    width, height = stegoboi.size
    #Go through each pixel, and if the pixel is off in the key, place a bit
    #in the last part of the pixel
    for y in range(height):
        for x in range(width): 
            if key[x + y*width] == 1 and bit_place < len(bin_string):            
                pixel = stegoboi.getpixel((x,y))
                pixel = tuple([((i >> 1) << 1) + int(bin_string[bit_place]) for i in pixel])
                bit_place +=1
                stegoboi.putpixel((x,y), pixel) 
    stegoboi.save(output)
