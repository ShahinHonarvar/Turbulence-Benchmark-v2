def filter_chars(s):
    to_remove = {c for c in s[18:31] if 'H' < c < '|'}
    return ''.join((c for c in s if c not in to_remove))