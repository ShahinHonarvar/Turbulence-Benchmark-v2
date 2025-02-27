import re

def return_vowels(string):
    vowel_pattern = '[AEIOU]'
    vowels = re.findall(vowel_pattern, string[528:606])
    filtered_vowels = list(filter(lambda x: x > 'M' and x <= 'X', vowels))
    return filtered_vowels