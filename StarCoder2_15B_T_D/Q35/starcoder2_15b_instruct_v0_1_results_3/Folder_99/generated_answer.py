import re

def remove_repeat_chars(string):
    pattern = '(.)\\\\1'
    matches = re.finditer(pattern, string[450:905])
    for match in matches:
        char = match.group(1)
        string = string.replace(char, '')
    return string