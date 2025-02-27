import re

def return_vowels(string):
    vowels = re.findall('[a-zA-Z]', string)
    return [vowel for vowel in vowels if vowel > 'U' and vowel <= 'l']