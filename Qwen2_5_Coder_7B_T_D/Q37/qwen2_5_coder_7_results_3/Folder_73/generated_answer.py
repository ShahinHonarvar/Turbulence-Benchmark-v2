def filter_chars(s):
    return ''.join((ch for ch in s if not (22 <= s.index(ch) <= 85 and '7' <= ch <= 'e')))