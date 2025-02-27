import re

def return_vowels(text):
    pattern = '[aeiou]'
    vowels = re.findall(pattern, text[24:68])
    filtered_vowels = list(filter(lambda vowel: vowel > 'f' and vowel <= '|', vowels))
    return filtered_vowels