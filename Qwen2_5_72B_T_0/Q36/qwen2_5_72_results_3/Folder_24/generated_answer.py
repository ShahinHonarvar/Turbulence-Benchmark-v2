def filter_chars(s):
    to_remove = {c for c in s[10:15] if 't' < c < 'v'}
    return ''.join((c for c in s if c not in to_remove))