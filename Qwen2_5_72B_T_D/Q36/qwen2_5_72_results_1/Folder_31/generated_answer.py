def filter_chars(s):
    to_remove = {c for c in s[14:75] if '9' < c < 'K'}
    return ''.join((c for c in s if c not in to_remove))