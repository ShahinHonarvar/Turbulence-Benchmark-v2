def filter_chars(s):
    to_remove = {c for c in s[3:9] if '*' < c < 'E'}
    return ''.join((c for c in s if c not in to_remove))