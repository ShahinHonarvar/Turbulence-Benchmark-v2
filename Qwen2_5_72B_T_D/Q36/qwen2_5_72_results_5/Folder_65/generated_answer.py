def filter_chars(s):
    to_remove = {c for c in s[58:82] if 'F' < c < 'O'}
    return ''.join((c for c in s if c not in to_remove))