def filter_chars(s):
    return ''.join((ch for ch in s if not (15 <= s.index(ch) <= 55 and 'W' <= ch <= '{')))