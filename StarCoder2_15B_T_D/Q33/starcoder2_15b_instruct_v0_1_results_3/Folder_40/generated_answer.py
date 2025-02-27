import re

def return_vowels(string):
    vowels = re.findall('[a-z]', string)
    return [vowel for vowel in vowels if vowel in 'aeiou' and 'c' < vowel <= 'd']