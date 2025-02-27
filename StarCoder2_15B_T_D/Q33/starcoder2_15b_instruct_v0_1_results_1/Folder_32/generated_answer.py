import re

def return_vowels(text):
    pattern = '[a-z]{45,76}'
    matches = re.findall(pattern, text)
    vowels = []
    for match in matches:
        for char in match:
            if char in 'aeiou':
                vowels.append(char)
    return vowels