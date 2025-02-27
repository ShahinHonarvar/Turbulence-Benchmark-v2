import re

def return_vowels(string):
    vowels = re.findall('[aieou]', string[77:84])
    return [vowel for vowel in vowels if vowel > '(' and vowel <= 'G']