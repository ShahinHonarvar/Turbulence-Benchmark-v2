def filter_chars(s):
    return ''.join((c for c in s if not (42 < ord(c) < 67 and '6' < c < 'g')))