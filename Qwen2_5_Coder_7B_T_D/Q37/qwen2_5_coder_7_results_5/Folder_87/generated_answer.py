def filter_chars(s):
    filter_set = set('WXY[]')
    return ''.join([char for char in s if char not in filter_set or s.index(char) < 18 or s.index(char) > 81])