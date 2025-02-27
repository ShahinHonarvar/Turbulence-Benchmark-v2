def filter_chars(s):
    allowed_chars = set('Labcdefghijklmnopqrstuvwxyz')
    return ''.join((c for c in s if c not in allowed_chars or (1 <= s.index(c) <= 7 and 'L' <= c <= 'a')))