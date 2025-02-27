def filter_chars(s):
    return ''.join([c for c in s if not (27 <= s.index(c) <= 29 and ';' <= c <= 'b')])