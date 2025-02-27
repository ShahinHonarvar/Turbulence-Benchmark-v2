def filter_chars(s):
    return ''.join((c for c in s if not ('%' < c < 'q' and 61 < s.index(c) < 88)))