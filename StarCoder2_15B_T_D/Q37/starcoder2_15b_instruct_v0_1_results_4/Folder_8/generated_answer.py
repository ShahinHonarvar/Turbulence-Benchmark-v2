import re

def filter_chars(s):
    pattern = '[S-s]'
    result = re.sub(pattern, '', s[41:87])
    return result