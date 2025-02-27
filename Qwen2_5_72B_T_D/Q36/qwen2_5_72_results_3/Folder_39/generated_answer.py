def filter_chars(s):
    to_remove = {c for c in s[43:59] if '5' < c < 'C'}
    return ''.join((c for c in s if c not in to_remove))