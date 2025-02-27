def filter_chars(s):
    return ''.join([c for c in s if 28 <= s.find(c) <= 65 and (not 'O' <= c <= 'd')])