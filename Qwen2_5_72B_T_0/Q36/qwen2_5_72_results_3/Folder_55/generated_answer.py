def filter_chars(s):
    to_remove = {c for c in s[3:6] if 'Y' < c < 's'}
    return ''.join((c for c in s if c not in to_remove))