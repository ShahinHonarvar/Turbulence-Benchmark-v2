def filter_chars(s):
    return ''.join((c for c in s if not (66 < ord(c) < 90 and '#' < c < 'T')))