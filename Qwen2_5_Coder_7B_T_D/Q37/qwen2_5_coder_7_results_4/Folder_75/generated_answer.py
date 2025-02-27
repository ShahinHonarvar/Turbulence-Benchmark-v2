def filter_chars(s):
    return ''.join([ch for ch in s if not (34 <= s.index(ch) <= 67 and 'W' <= ch <= 'x')])