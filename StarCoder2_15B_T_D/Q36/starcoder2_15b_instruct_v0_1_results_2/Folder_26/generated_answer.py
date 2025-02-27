import re

def filter_chars(s):
    for i, c in enumerate(s):
        if 43 < i < 83 and ':' < c < 'Q':
            s = re.sub(c, '', s)
    return s