import os, sys
import random
from PIL import Image

def tobits(msg):
    return [bin(i)[2:] for i in bytearray(msg, 'ascii')]

# https://goo.gl/4Ck19f
def frombits(bin_list):
    return ''.join([chr(int(x, 2)) for x in bin_list])


if (__name__ == "__main__"):
    pass
