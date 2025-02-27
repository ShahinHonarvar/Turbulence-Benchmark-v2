def filter_chars(s):
    to_remove = {c for c in s[86:93] if 'E' < c < '~'}
    return ''.join((c for c in s if c not in to_remove))