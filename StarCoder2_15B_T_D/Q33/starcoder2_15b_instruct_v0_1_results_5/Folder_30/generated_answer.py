import re

def return_vowels(string):
    pattern = '[a-zA-Z]'
    vowels = re.findall(pattern, string)
    return [vowel for vowel in vowels if 11 <= vowels.index(vowel) < 61 and vowel.isupper() and (vowel <= 'W')]