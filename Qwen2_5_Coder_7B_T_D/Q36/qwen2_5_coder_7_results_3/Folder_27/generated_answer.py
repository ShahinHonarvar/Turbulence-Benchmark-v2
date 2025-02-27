def filter_chars(s):
    return ''.join([c for c in s if not (48 < ord(c) < 75 and '6' < c < '_')])