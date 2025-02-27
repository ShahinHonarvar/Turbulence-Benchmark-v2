def filter_chars(s):
    to_remove = {c for c in s[44:59] if '/' < c < '6'}
    return ''.join((c for c in s if c not in to_remove))