import re

def return_vowels(text):
    pattern = '[a-zA-Z]'
    vowels = re.findall(pattern, text[63:79])
    return [vowel for vowel in vowels if vowel.isalpha() and vowel.upper() > 'D' and (vowel.upper() <= 'Y')]