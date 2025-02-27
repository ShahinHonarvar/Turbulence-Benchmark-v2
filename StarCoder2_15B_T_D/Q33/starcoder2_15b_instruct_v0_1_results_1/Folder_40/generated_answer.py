import re

def return_vowels(string):
    vowels = re.findall('[aeiou]', string)
    return [vowel for vowel in vowels if vowels.index(vowel) >= 2 and vowels.index(vowel) < 7 and (vowel > '^') and (vowel <= 'd')]