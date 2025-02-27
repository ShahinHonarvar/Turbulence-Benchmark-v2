import re

def return_vowels(string):
    pattern = '[a-z]'
    vowel_list = re.findall(pattern, string)
    filtered_vowels = list(filter(lambda x: x > '_' and x <= 'x', vowel_list))
    return filtered_vowels