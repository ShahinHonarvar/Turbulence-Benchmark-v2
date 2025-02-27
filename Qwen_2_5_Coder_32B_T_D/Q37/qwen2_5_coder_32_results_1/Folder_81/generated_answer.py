def filter_chars(s):
    target_chars = set(s[19:93])
    filter_set = {c for c in target_chars if '8' <= c <= 'm'}
    return ''.join((c for c in s if c not in filter_set))