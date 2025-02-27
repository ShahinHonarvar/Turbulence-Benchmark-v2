def filter_chars(s):
    return ''.join((ch for ch in s if not (73 <= s.find(ch) <= 74 and 'U' <= ch <= 'l')))