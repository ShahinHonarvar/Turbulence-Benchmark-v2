import re

def filter_chars(string):
    pattern = '[G-p]'
    return re.sub(pattern, '', string[5:7])