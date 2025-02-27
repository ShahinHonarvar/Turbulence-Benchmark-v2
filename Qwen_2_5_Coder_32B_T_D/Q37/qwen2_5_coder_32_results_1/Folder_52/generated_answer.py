def filter_chars(s):
    target_chars = set(s[54:84])
    filter_set = {c for c in target_chars if 'j' <= c <= 'v'}
    return ''.join((c for c in s if c not in filter_set))