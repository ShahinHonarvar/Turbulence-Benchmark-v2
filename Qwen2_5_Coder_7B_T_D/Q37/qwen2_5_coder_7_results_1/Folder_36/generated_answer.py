def filter_chars(s):
    return ''.join([c for c in s if not (259 <= s.index(c) <= 502 and ',' <= c <= '3')])