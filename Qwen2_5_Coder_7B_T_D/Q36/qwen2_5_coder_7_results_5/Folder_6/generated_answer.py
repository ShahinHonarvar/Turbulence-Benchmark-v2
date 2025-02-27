def filter_chars(s):
    return ''.join((c for c in s if 31 < ord(c) < 70 and (not (c > 'B' and c < 'v'))))