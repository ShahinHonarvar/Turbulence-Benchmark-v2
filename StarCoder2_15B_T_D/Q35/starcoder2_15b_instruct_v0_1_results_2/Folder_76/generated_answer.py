import re

def remove_repeat_chars(string):
    pattern = re.compile('(.).*\\\\1', re.DOTALL)
    matches = pattern.finditer(string[330:543])
    repeated_chars = [match.group(1) for match in matches]
    for char in repeated_chars:
        string = string.replace(char, '')
    return string