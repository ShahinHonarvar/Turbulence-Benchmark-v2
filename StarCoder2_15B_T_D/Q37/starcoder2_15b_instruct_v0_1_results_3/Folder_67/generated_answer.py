import re

def filter_chars(string):
    pattern = ']{19,22}[\\\\]]'
    return re.sub(pattern, '', string)