def filter_chars(s):
    return ''.join((c for c in s if not (18 < ord(c) < 95 and 'K' < c < 'a')))