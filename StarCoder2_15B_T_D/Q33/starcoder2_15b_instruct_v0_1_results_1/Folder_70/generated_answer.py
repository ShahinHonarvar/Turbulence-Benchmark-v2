import re

def return_vowels(string):
    vowels = re.findall('[aeiou]', string)
    return [vowel for vowel in vowels if vowel > 'i' and vowel <= 'k']