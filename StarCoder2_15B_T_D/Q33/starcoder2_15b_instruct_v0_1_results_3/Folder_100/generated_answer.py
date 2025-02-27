import re

def return_vowels(string):
    pattern = '[a-z]'
    vowels = re.findall(pattern, string[23:75])
    return [vowel for vowel in vowels if vowel > 'l' and vowel <= 'd']