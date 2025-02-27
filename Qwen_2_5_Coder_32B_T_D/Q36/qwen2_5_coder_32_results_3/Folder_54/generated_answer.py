def filter_chars(s):
    target_chars = set(s[18:38])
    filter_set = {c for c in target_chars if ')' < c < 'P'}
    return ''.join((c for c in s if c not in filter_set))