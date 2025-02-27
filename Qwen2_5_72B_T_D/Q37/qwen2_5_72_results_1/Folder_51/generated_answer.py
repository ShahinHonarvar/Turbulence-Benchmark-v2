def filter_chars(s):
    to_remove = {c for c in s[36:41] if 'H' <= c <= 'e'}
    return ''.join((c for c in s if c not in to_remove))