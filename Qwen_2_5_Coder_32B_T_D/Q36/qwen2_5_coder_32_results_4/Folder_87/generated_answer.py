def filter_chars(s):
    t = ''.join([c for c in s if not (32 < ord(c) < 61 and '3' < c < 'D')])
    return t