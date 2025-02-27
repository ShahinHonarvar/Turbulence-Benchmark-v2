import re

def filter_chars(string):
    pattern = '[>B-r<]'
    result = re.sub(pattern, '', string)
    return result