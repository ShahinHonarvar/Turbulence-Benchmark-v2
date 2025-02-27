def filter_chars(s):
    a = set(s[2:4])
    b = {c for c in a if '5' <= c <= '_'}
    return ''.join((c for c in s if c not in b))