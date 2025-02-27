import re

def return_vowels(string):
    pattern = '[a-z]{45,76}'
    matches = re.findall(pattern, string)
    vowels = []
    for match in matches:
        for char in match:
            if char in 'aeiou' and char > 'b' and (char <= 'z'):
                vowels.append(char)
    return vowels