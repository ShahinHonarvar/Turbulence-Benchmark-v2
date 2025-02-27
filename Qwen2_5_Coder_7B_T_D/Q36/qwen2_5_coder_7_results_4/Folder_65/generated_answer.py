def filter_chars(s):
    return ''.join((c for c in s if not (58 < ord(c) < 82 and 'F' < c < 'O')))