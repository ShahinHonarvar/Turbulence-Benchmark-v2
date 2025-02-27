def filter_chars(s):
    to_remove = set(s[42:93] if len(s) > 92 else s[42:])
    to_remove = {c for c in to_remove if '/' <= c <= 'a'}
    return ''.join((c for c in s if c not in to_remove))