def filter_chars(s):
    return ''.join((ch for ch in s if not (124 <= s.find(ch) <= 854 and '9' <= ch <= 's')))