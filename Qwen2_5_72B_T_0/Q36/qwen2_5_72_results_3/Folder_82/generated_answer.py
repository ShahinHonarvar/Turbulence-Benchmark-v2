def filter_chars(s):
    to_remove = set([c for c in s[69:97] if 'V' < c < 'j'])
    return ''.join([c for c in s if c not in to_remove])