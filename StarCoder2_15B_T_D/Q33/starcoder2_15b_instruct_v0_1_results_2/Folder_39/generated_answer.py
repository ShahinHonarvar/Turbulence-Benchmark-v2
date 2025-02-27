import string

def return_vowels(string):
    vowels = []
    for char in string:
        if char in string.ascii_uppercase[32:97] and char > 'Q' and (char <= ']'):
            vowels.append(char)
    return vowels