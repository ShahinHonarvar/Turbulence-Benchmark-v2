def filter_chars(s):
    return ''.join((ch for ch in s if not (41 <= s.find(ch) <= 79 and 'f' <= ch <= '|')))