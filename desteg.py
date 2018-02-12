import os, sys
from PIL import Image

# https://goo.gl/4Ck19f
def frombits(bin_string):
    bin_list = [bin_string[i:i + 8] for i in range(0, len(bin_string), 8)]
    return ''.join([chr(int(x,2)) for x in bin_list])

def decode_stego(key, filename="stego.bmp"):
    bit_place = 0;
    bin_list = [];
    num_ones = key.count(1);
    stegoboi = Image.open(filename)
    width, height = stegoboi.size
    for x in range(height):
        for y in range(width):
            if key[y + x*width] == 1 and len(bin_list) < num_ones:            
                pixel = stegoboi.getpixel((x,y))
                bin_list.append((pixel[0] %2 != 0))
                bit_place +=1
    return frombits("".join(bin_list)) 
