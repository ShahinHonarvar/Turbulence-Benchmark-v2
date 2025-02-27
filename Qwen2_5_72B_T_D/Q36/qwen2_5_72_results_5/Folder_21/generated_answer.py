def filter_chars(s):
    to_remove = {c for c in s[219:403] if '*' < c < '7'}
    return ''.join((c for c in s if c not in to_remove))