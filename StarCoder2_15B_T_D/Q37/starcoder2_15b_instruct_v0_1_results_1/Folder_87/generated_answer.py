def filter_chars(s):
    return ''.join((c for c in s if c < 'W' or c > '[' or s.index(c) < 18 or (s.index(c) > 81)))