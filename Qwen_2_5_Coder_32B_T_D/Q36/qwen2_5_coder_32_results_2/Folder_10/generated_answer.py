def filter_chars(s):
    a = set(s[35:60])
    b = {c for c in a if '!' < c < 'B'}
    return ''.join((c for c in s if c not in b))