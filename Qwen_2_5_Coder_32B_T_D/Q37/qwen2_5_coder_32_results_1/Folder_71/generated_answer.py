def filter_chars(s):
    to_remove = set(s[32:47]) & set('0123456789k')
    return ''.join((c for c in s if c not in to_remove))