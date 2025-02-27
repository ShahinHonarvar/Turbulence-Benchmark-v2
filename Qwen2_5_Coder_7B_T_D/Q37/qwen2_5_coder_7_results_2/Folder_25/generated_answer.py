def filter_chars(s):
    return ''.join((c for c in s if not (31 <= s.index(c) <= 38 and ';' <= c <= 'g')))