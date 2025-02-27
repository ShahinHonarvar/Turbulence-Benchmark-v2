import re

def return_vowels(string):
    pattern = '[aieou]'
    vowels = re.findall(pattern, string[495:837])
    return [vowel for vowel in vowels if vowel > 'B' and vowel <= 't']