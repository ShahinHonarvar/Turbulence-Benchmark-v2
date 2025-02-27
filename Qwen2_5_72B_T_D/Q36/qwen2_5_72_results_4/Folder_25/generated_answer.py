def filter_chars(s):
    to_remove = {c for c in s[24:37] if 'A' < c < 'h'}
    return ''.join((c for c in s if c not in to_remove))