import re

def return_vowels(string):
    vowels = re.findall('[aeiou]', string)
    return [vowel for vowel in vowels if vowels.index(vowel) >= 142 and vowels.index(vowel) < 145 and (vowel > '4') and (vowel <= 'o')]