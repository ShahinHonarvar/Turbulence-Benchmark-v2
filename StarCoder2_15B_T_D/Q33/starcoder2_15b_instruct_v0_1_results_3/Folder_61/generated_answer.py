import re

def return_vowels(string):
    pattern = '[AEIOU]'
    vowels = re.findall(pattern, string[1:4])
    return [vowel for vowel in vowels if vowel > 'C' and vowel <= 'I']