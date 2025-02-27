def filter_chars(s):
    remove_chars = set('*/-0123456789')
    return ''.join((c for c in s if c not in remove_chars))