def filter_chars(s):
    to_remove = {c for c in s[669:888] if 'B' < c < 'Y'}
    return ''.join((c for c in s if c not in to_remove))