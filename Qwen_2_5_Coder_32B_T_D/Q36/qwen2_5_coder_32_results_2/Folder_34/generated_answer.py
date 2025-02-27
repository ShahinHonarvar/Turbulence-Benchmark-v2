def filter_chars(s):
    target_chars = set(s[10:79])
    to_remove = {c for c in target_chars if '?' < c < 'm'}
    return ''.join((c for c in s if c not in to_remove))