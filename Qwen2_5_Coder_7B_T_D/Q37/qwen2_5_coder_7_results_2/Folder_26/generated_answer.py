def filter_chars(s):
    return ''.join((ch for ch in s if not (20 <= s.index(ch) <= 62 and 'i' <= ch <= 'k')))