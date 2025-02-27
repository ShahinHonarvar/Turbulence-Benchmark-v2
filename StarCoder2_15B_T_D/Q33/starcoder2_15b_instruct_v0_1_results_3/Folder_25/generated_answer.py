import re

def return_vowels(text):
    vowels = re.findall('[a-z]', text[28:76])
    return [vowel for vowel in vowels if vowel > '+' and vowel <= 'z']