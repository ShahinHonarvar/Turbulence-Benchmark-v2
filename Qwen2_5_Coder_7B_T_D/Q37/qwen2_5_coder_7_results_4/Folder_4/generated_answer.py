def filter_chars(s):
    return ''.join([c for c in s if not (19 <= s.find(c) <= 33 and 'S' <= c <= '{')])