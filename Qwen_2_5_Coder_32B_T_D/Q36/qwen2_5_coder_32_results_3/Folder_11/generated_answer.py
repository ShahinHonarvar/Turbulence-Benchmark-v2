def filter_chars(s):
    to_remove = set(s[86:93])
    filtered = {c for c in to_remove if 'E' < c < '~'}
    return ''.join((c for c in s if c not in filtered))