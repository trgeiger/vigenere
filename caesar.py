def alphabet_position(character):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    character = character.lower()
    return(alpha.index(character))

def rotate_string_13(text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    capalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_text = ""
    for letter in text:
        if letter == " ":
            new_text += " "
        elif letter in capalpha:
            index = alphabet_position(letter)
            index = (index + 13) % 26
            new_text = new_text + capalpha[index]
        else:
            index = alphabet_position(letter)
            index = (index + 13) % 26
            new_text = new_text + alpha[index]
    return new_text

def rotate_character(char, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    capalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_char = ""
    if char in capalpha:
        index = alphabet_position(char)
        index = (index + rot) % 26
        new_char = capalpha[index]
    elif char in alpha:
        index = alphabet_position(char)
        index = (index + rot) % 26
        new_char = alpha[index]
    else:
        new_char = char
    return new_char

def rotate_string(text, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    capalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_text = ""
    for char in text:
        if char in alpha:
            index = alphabet_position(char)
            index = (index + rot) % 26
            new_text = new_text + alpha[index]
        elif char in capalpha:
            index = alphabet_position(char)
            index = (index + rot) % 26
            new_text = new_text + capalpha[index]
        else:
            new_text = new_text + char
    return new_text
