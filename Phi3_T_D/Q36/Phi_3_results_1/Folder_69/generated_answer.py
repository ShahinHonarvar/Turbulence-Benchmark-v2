def filter_chars(s):
    return ''.join([c for c in s if c < '%' or c > 'U' or (not 343 < s.index(c) < 665)])