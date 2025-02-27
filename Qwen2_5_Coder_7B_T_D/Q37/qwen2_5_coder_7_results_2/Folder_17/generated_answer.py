def filter_chars(s):
    return ''.join((ch for ch in s if not (27 <= s.find(ch) <= 29 and ';' <= ch <= 'b')))