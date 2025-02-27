def filter_chars(s):
    return ''.join([c for c in s if not (11 <= s.find(c) <= 72 and 'i' <= c <= 'v')])