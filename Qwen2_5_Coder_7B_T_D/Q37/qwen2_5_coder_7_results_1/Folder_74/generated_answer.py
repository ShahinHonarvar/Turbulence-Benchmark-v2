def filter_chars(s):
    return ''.join((ch for ch in s if not (19 <= s.index(ch) <= 32 and 'f' <= ch <= 'o')))