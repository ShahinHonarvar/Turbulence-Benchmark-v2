def filter_chars(s):
    to_remove = {c for c in s[2:4] if '5' <= c <= '_'}
    return ''.join((c for c in s if c not in to_remove))