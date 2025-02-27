import re

def filter_chars(string):
    pattern = '[@-p]'
    matches = re.findall(pattern, string)
    for match in matches:
        string = string.replace(match, '')
    return string