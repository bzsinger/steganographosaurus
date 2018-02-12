import os, sys
from PIL import Image

# https://goo.gl/4Ck19f
def frombits(bin_list):
    bin_list = [bin_list[pos:pos + 8] for pos in range(0, len(blist), 8)]
    return ''.join([chr(int(x) for x in bin_list])

def decode_stego(key, filename):
    bit_place = 0;
    bin_list = [];
    numOne = key.count(1);
    stegoPic = Image.open(filename)
    for x in range(height):
        for y in range(width): 
            #put this in a function to break out of it
            if key[y + x*width] == 0 and len(bin_list) < numOne:            
                pixelO = stego2boi.getpixel((x,y))
                bin_list.append((pixelO[0] %2 != 0))
                bit_place +=1
    return frombits(bin_list) 

