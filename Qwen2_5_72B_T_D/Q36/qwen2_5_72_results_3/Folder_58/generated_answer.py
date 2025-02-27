def filter_chars(s):
    to_remove = {c for c in s[318:337] if 'B' < c < 'z'}
    return ''.join((c for c in s if c not in to_remove))