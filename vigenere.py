from caesar import alphabet_position, rotate_character
import sys

def vigenere(text, key):
    #declaring some constants
    alpha = "abcdefghijklmnopqrstuvwxyz"
    capalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.lower()
    new_text = ""

    lenkey = len(key)
    lentext = 0
    for char in text:
        if char.isalpha():
            lentext += 1

    multkey = key * (lentext // lenkey) + key[:(lentext % lenkey)]

    i = 0
    for char in text:
        if char.isalpha() == False:
            new_text = new_text + char
        else:
            rot = alphabet_position(multkey[i])
            new_text = new_text + rotate_character(char, rot)
            i += 1

    return new_text

print(vigenere(input("Enter your secret message: "), sys.argv[1]))
