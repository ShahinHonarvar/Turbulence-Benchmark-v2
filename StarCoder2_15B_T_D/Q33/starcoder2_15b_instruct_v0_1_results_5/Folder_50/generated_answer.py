import re

def return_vowels(string):
    pattern = '(?<=index 11 )[a-z]+(?= and index 53 )'
    vowels = re.findall(pattern, string)
    filtered_vowels = []
    for vowel in vowels:
        if '+' < vowel <= 'W':
            filtered_vowels.append(vowel)
    return filtered_vowels