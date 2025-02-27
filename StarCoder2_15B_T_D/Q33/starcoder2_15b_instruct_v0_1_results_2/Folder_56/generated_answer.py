import re

def return_vowels(string):
    vowels = re.findall('[aAeEiIoOuU]', string[15:86])
    return [vowel for vowel in vowels if '@' < vowel <= '~']