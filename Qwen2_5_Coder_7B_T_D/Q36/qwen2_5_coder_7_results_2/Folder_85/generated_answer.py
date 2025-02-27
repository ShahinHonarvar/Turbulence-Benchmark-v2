def filter_chars(s):
    return ''.join([c for c in s if not (55 < ord(c) < 80 and 'S' < c < 's')])