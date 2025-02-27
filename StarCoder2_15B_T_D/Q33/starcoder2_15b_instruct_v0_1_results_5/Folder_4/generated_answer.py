import re

def return_vowels(string):
    vowels = re.findall('[a-xA-X]', string[40:91])
    return [vowel for vowel in vowels if vowel in 'aeiou']