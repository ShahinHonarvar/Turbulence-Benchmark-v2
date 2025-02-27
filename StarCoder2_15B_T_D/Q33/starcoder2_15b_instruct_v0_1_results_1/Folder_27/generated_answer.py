import re

def return_vowels(string):
    pattern = '[a-f]{1}'
    vowels = re.findall(pattern, string[29:31])
    return vowels