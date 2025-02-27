def filter_chars(s):
    filter_set = set(s[42:98])
    filter_set = {c for c in filter_set if '*' <= c <= 'b'}
    return ''.join((c for c in s if c not in filter_set))