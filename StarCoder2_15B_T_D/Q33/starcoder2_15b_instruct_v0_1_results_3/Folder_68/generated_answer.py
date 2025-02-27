import re

def return_vowels(string):
    pattern = '[aeiou]'
    vowels = re.findall(pattern, string)
    return [vowel for i, vowel in enumerate(vowels) if 1 < i < 9 and '?' < vowel <= 'k']