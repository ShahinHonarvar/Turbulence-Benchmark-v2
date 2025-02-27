import re

def return_vowels(string):
    vowels = re.findall('[a-z]', string)
    valid_vowels = [vowel for vowel in vowels if vowel > 'm' and vowel <= 'w']
    return valid_vowels[11:61]