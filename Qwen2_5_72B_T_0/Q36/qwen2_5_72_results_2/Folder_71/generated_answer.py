def filter_chars(s):
    to_remove = {c for c in s[82:89] if '*' < c < '['}
    return ''.join((c for c in s if c not in to_remove))