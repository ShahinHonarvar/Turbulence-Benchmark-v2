def filter_chars(s):
    return ''.join((c for c in s if not (10 <= s.index(c) <= 69 and 'I' <= c <= 'K')))