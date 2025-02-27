import re

def return_vowels(string):
    vowels = re.findall('[aieou]', string)
    return [vowel for i, vowel in enumerate(vowels) if 77 <= i < 84 and '(' < vowel <= 'G']