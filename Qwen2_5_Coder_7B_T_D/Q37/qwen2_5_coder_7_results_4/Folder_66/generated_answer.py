def filter_chars(s):
    return ''.join((c for c in s if (c < 'c' or c > 'i') or (27 > s.index(c) or s.index(c) > 85)))