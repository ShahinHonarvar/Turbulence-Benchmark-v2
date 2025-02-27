def filter_chars(s):
    return ''.join((ch for ch in s if not (54 <= s.index(ch) <= 62 and ')' <= ch <= '9')))