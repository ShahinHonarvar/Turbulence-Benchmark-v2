def filter_chars(s):
    return ''.join((c for c in s if not (35 <= s.index(c) <= 89 and 'E' <= c <= 't')))