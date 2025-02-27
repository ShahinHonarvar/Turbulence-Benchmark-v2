def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (49 < ord(c) < 58 and 'J' < c < 'a')))