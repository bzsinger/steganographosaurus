# steganographosaurus
Hides a message in the least significant bits of a png image

| Algorithm             | File Format |
|:---------------------:|:-----------:|
| Least-Significant Bit | PNG         |

## Proposal
Our group members will embed our names into the below PNG image of a stegosaurus. We will create a program that can both embed a message into an image using the image’s least significant bits and extract a message from the least significant bits of a given image. Our program will also create a random key that indicates which pixels we will be utilizing and require a person attempting to decrypt the message to provide said key.

![Stego Boi](https://github.com/bzsinger/steganographosaurus/raw/master/stegosaurus.png "Stego Boi")

## Run Instructions
```bash
git clone git@github.com:bzsinger/steganographosaurus.git
cd steganographosaurus
# encrypt
python steggy.py -e "<message>" <input_picture_path> <OPTIONAL_key>
# decrypt
python steggy.py -d <input_picture_path> <key>
```

### Example
```bash
python steggy.py -e "Sue Anne Davis, Akash Kwatra, Benny Singer" ./stegosaurus.png
python steggy.py -d ./stego.bmp ./key.bmp
```

### Group Members
 - [Akash Kwatra](https://github.com/akashkw)

- [Sue Anne Davis](https://github.com/tiramisueanne)

- [Benny Singer](https://github.com/bzsinger)
