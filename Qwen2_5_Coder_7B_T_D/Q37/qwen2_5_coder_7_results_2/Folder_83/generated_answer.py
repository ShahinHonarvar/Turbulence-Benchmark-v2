def filter_chars(s):
    return ''.join([c for c in s if not (29 <= s.find(c) <= 79 and 'K' <= c <= 'z')])