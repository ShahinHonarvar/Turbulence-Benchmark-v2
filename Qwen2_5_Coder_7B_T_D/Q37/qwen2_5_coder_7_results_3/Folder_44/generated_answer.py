def filter_chars(s):
    return ''.join([c for c in s if not (21 <= s.find(c) <= 43 and '+' <= c <= '8')])