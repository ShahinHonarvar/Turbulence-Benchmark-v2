import re

def return_vowels(string):
    vowels = re.findall('[a-zA-Z]', string)
    return [vowel for vowel in vowels if 74 <= vowels.index(vowel) < 96 and vowel.upper() > 'I' and (vowel.upper() <= 'X')]