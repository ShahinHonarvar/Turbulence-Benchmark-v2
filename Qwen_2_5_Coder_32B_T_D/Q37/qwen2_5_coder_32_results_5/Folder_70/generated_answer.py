def filter_chars(s):
    a = set(s[515:539])
    b = {c for c in a if '+' <= c <= '}'}
    return ''.join((c for c in s if c not in b))