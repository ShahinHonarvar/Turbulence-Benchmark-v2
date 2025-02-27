import re

def filter_chars(s):
    pattern = '[G-p]'
    s = re.sub(pattern, '', s)
    return s