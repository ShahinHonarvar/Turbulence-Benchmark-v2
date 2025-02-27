def filter_chars(s):
    return ''.join((c for c in s if 12 <= s.index(c) <= 25 and 'P' <= c <= 'x' or s.index(c) < 12 or s.index(c) > 25))