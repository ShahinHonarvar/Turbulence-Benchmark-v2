def filter_chars(s):
    return ''.join((c for c in s if not (31 < ord(c) < 73 and 'M' < c < 'j')))