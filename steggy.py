import os, sys, time
import random
from PIL import Image
from desteg import decode_stego
from ensteg import write_stego
from keyio import read_key, generate_key


if(__name__ == "__main__"):
    print("\nWelcome to Jurassic Park!!\n")
    print("\nToday we will visit the stegonographasurus :D\n")
    print("\nThen we will visit our security team, Dennis Nedry, to talk about how to keep the park running smoothly ;) \n")
    time.sleep(1000)
    print("\nSo here is the steganographastorus! Legend has it, he will keep secrets for you :O\n")
    print("\nWould you like to tell him something? Or is is there something he has for you?\n")


    while (True):
        operation = input("*Type encrypt or decrypt pls me too thanks* :: ").upper()
        if 'D' in operation:
            operation = 'D'
            break
        if 'E' in operation:
            operation = 'E'
            break
        print("\nYo wtf is that???, I'll try again my dude...\n")

    while (True):

        if operation == 'E':
            key_name = read_key(input("\nWhat would you like to name the key file :: "))
            output_name = read_key(input("\nWhat would you like to name the encrypted image :: "))
            image_file = read_key(input("\nWhat image file would you like to encrypt? :: "))
            message = read_key(input("\nWhat is your message? :: "))
            print("\n\nGenerating Random Key...\n")
            time.sleep(1000)
            generate_key(image_file, message, key_name)
            print("\nKey saved as {}\n".format(key_name))
            key = read_key(key_name)
            time.sleep(500)
            print("\nEncrypting image...\n")
            time.sleep(500)
            write_stego(key, message, image_file, output_name)
            print("\nEncrypted image saved as {}\n".format(output_name))
            break

        else:
            key = read_key(input("\nPlease enter key file name :: "))
            image_name = input("\nPlease enter encrypted image name :: ")
            print("\n\nYour message is :: {}".format(decode_stego(key, image_name)))
            break

        print("\nI'm sorry what was that??\n")
    
    print("\nI hope you had a wonderful time visiting the steganographotsowetwnwknlenwwrjoos!!!\n")
    print("\nGoodbye!\n")
