def filter_chars(s):
    if len(s) < 899:
        return s
    target_chars = set(s[379:900])
    filter_set = {c for c in target_chars if 'M' <= c <= 'v'}
    return ''.join((c for c in s if c not in filter_set))