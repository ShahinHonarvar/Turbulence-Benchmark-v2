import re

def return_vowels(string):
    vowels = re.findall('[a-zA-Z]', string[10:82])
    return [vowel for vowel in vowels if vowel > '$' and vowel <= '@']