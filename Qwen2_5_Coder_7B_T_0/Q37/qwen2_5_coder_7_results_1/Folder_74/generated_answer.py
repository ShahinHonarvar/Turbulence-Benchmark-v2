def filter_chars(s):
    return ''.join((c for c in s if not (19 <= s.index(c) <= 32 and 'f' <= c <= 'o')))