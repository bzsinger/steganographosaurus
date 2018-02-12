import os, sys
from PIL import Image

def tobits(message):
    return "".join("{:08b}".format(i) for i in bytearray(message, 'ascii')])

def write_stego(key, message, filename):
    bit_place = 0
    bin_list = tobits(message)
    stegoboi = Image.open(filename)
    width, height = stegoboi.size
    #Go through each pixel, and if the pixel is off in the key, place a bit
    #in the last part of the pixel
    for x in range(height):
        for y in range(width): 
            if key[y + x*width] == 1 and bit_place < len(bin_list):            
                pixelO = stegoboi.getpixel((x,y))
                #print(int(bin_list[bit_place]))
                pixelO = tuple([((i >> 1) << 1) + int(bin_list[bit_place]) for i in pixelO])
                bit_place +=1
                stego2boi.putpixel((x,y), pixelO) 
    stego2boi.save("stego2.bmp")

