import re

def return_vowels(text):
    pattern = '[/a-zA-Z]'
    vowels = re.findall(pattern, text[21:59])
    return vowels