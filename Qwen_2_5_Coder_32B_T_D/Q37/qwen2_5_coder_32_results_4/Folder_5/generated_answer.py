def filter_chars(s):
    target_chars = set(s[24:83])
    filter_set = {c for c in target_chars if '5' <= c <= '<'}
    return ''.join((c for c in s if c not in filter_set))