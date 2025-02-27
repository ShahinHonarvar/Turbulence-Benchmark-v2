def filter_chars(s):
    target_range = s[19:32 + 1]
    target_chars = {c for c in target_range if 'f' <= c <= 'o'}
    return ''.join((c for c in s if c not in target_chars))