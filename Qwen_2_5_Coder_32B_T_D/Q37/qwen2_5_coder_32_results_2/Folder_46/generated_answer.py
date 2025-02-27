def filter_chars(s):
    target_chars = set(s[11:73])
    target_chars = {c for c in target_chars if 'i' <= c <= 'v'}
    return ''.join((c for c in s if c not in target_chars))