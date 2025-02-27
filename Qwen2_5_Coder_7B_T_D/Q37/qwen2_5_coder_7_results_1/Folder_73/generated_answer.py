def filter_chars(s):
    char_set = set('789abcdefgh')
    return ''.join((c for c in s if c not in char_set or s.index(c) < 22 or s.index(c) > 85))