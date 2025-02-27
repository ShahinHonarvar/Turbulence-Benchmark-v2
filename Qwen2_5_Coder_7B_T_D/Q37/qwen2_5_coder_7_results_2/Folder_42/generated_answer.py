def filter_chars(s):
    return ''.join((ch for ch in s if not (73 <= s.index(ch) <= 74 and 'U' <= ch <= 'l')))