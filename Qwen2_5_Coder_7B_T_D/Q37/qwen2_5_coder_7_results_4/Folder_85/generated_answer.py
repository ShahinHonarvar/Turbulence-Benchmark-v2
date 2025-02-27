def filter_chars(s):
    return ''.join((ch for ch in s if not (28 <= s.index(ch) <= 65 and 'O' <= ch <= 'd')))