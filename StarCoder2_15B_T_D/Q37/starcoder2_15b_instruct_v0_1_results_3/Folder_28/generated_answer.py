import re

def filter_chars(s):
    pattern = '[!-T]'
    return re.sub(pattern, '', s[20:80])