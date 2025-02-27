def filter_chars(s):
    a = set(s[219:403])
    b = {c for c in a if '*' < c < '7'}
    return ''.join((c for c in s if c not in b))