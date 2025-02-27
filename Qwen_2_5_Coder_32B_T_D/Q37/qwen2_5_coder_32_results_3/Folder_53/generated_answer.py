def filter_chars(s):
    target_chars = set(s[83:99 + 1]) & set(range(ord('*'), ord('j') + 1))
    return ''.join((c for c in s if c not in target_chars))