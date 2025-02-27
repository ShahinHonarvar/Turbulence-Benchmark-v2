def filter_chars(s):
    if len(s) < 833:
        return s
    target_chars = set(s[722:833])
    filter_set = {c for c in target_chars if 'K' <= c <= 'm'}
    return ''.join((c for c in s if c not in filter_set))