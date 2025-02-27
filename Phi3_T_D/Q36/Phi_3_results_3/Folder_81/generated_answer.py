def filter_chars(s):
    return s.translate({ord(c): None for c in s[51:76] if c > '5' and c < 'f'})