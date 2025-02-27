def filter_chars(s):
    return ''.join((c for c in s if not (45 < ord(c) < 57 and 'F' < c < 'n')))