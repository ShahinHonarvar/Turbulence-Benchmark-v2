def filter_chars(s):
    return ''.join([c for c in s if not (7 <= s.find(c) <= 8 and 'B' <= c <= 'H')])