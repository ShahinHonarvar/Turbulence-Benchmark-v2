def filter_chars(s):
    filtered_chars = set('abcdefghijklmnopqrstuvwxyz*')
    return ''.join((c for c in s if c not in filtered_chars or (42 <= s.index(c) <= 97 and '*' <= c <= 'b')))