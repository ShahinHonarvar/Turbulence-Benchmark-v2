def filter_chars(s):
    to_remove = {c for c in s[46:68] if 'H' < c < 's'}
    return ''.join((c for c in s if c not in to_remove))