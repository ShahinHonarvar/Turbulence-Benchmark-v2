def filter_chars(s):
    return ''.join((c for c in s if not ('-' < c < 'L' and 1 < s.index(c) < 7)))