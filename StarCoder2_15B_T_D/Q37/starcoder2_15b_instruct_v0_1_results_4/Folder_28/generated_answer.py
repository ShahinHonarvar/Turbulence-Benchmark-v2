def filter_chars(s):
    return ''.join((c for c in s if c < '!' or c > 'T' or s.index(c) < 20 or (s.index(c) > 79)))