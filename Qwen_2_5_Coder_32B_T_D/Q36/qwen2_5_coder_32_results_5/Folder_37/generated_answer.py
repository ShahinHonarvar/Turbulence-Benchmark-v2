def filter_chars(s):
    to_remove = set(s[44:59]) & set('012345')
    return ''.join((c for c in s if c not in to_remove))