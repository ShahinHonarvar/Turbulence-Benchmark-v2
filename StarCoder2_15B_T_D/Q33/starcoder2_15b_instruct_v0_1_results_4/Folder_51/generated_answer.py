import re

def return_vowels(string):
    vowels = re.findall('[AEIOU]', string[56:68])
    return [vowel for vowel in vowels if vowel > 'M' and vowel <= 'X']