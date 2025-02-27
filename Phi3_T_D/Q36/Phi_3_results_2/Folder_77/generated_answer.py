def filter_chars(s):
    exclude_range = s[221:419]
    exclude_set = {c for c in exclude_range if 'a' <= c <= 'u'}
    return ''.join([c for c in s if c not in exclude_set])