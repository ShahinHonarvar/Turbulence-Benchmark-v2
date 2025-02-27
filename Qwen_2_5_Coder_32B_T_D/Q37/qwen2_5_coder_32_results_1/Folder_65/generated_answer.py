def filter_chars(s):
    to_remove = set(s[61:71])
    to_remove = {c for c in to_remove if '0' <= c <= '@'}
    return ''.join((c for c in s if c not in to_remove))