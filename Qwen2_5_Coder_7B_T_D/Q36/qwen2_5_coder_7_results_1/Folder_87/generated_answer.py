def filter_chars(s):
    return ''.join([c for c in s if not (32 < ord(c) < 62 and '3' < c < 'D')])