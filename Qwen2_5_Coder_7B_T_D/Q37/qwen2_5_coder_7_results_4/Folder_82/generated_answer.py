def filter_chars(s):
    return ''.join((c for c in s if not (12 <= s.index(c) <= 25 and 'P' <= c <= 'x')))