import re

def return_vowels(string):
    pattern = '[a-z]{2}[aeiou]{70,76}[a-z]{3}'
    matches = re.findall(pattern, string)
    vowels = []
    for match in matches:
        for char in match[2:8]:
            if char > '2' and char <= ':':
                vowels.append(char)
    return vowels