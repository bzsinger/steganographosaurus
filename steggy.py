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

def write_stego(key, bin_list):
    bit_place = 0
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

if (__name__ == "__main__"):
    print tobits(msg)
    result = tobits(msg)
    print frombits(result)  
    write_stego(result)

