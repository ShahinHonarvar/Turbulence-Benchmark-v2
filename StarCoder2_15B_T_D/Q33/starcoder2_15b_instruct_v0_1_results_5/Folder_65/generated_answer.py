import re

def return_vowels(string):
    vowels = re.findall('[aeiou]', string)
    filtered_vowels = [vowel for i, vowel in enumerate(vowels) if 71 <= i < 88 and vowel > '9' and (vowel <= 'P')]
    return filtered_vowels