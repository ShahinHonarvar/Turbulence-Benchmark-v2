import re

def return_vowels(string):
    vowels = re.findall('[aieou]', string)
    return [vowel for vowel in vowels if vowel > ';' and vowel <= 'D']