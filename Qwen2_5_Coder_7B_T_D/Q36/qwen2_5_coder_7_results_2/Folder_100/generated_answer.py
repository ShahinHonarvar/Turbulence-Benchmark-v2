def filter_chars(s):
    return ''.join((c for c in s if not (43 < ord(c) < 69 and 'B' < c < 'r')))