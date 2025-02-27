def filter_chars(s):
    to_remove = {c for c in s[81:86] if '!' < c < 's'}
    return ''.join((c for c in s if c not in to_remove))