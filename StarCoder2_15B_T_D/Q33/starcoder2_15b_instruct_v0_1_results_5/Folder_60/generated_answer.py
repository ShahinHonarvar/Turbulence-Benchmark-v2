import re

def return_vowels(string):
    pattern = '[N-U]'
    vowels = re.findall(pattern, string[24:59])
    return vowels