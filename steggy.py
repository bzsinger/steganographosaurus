import os, sys
import random
from desteg import decode_stego
from ensteg import write_stego
from keyio import read_key, generate_key

if __name__ == '__main__':
    input_file = None
    output_file = None

    if len(sys.argv) < 4:
        raise IOError('\nProper usage: \npython steggy.py -e "<message>" <input_picture_path> <OPTIONAL_key> \n or \n python steggy.py -d <input_picture_path> <key>')

    message = None
    input_picture_path = None
    key = None

    if sys.argv[1] == '-e':
        message = sys.argv[2]
        input_picture_path = sys.argv[3]
        if len(sys.argv) >= 5:
            key = sys.argv[4]

    if sys.argv[1] == '-d':
        input_picture_path = sys.argv[2]
        key = sys.argv[3]


    key_list = generate_key(input_picture_path, message) if key is None else read_key(key)

    if sys.argv[1] == '-e':
        write_stego(key_list, message, input_picture_path)
    elif sys.argv[1] == '-d':
        output_text = decode_stego(key_list, input_picture_path)
        print(output_text)
    else:
        raise IOError('\nProper usage: \npython steggy.py -e "<message>" <input_picture_path> <OPTIONAL_key> \n or \n python steggy.py -d <input_picture_path> <key>')
