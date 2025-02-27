import re

def return_vowels(text):
    vowels = re.findall('[a-z]', text)
    return [vowel for vowel in vowels if vowel > 'w' and vowel <= 'v']