def filter_chars(s):
    to_remove = {c for c in s[55:84] if ';' < c < 'z'}
    return ''.join((c for c in s if c not in to_remove))