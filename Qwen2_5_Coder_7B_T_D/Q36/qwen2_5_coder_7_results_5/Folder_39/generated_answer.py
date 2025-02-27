def filter_chars(s):
    return ''.join((c for c in s if not (43 < ord(c) < 59 and '5' < c < 'C')))