import re

def filter_chars(s):
    pattern = ';<=c<=b'
    matches = re.findall(pattern, s)
    for match in matches:
        s = s.replace(match, '')
    return s