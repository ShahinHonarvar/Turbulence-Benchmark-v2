import re

def filter_chars(s):
    pattern = '=[!-@]'
    return re.sub(pattern, '', s[43:81])