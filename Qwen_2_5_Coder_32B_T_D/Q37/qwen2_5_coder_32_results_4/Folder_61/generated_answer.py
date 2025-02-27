def filter_chars(s):
    target_chars = set(s[5:7])
    valid_chars = {c for c in target_chars if 'G' <= c <= 'p'}
    return ''.join((c for c in s if c not in valid_chars))