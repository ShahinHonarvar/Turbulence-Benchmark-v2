def filter_chars(s):
    target_chars = [c for c in s[3:5] if 'Y' < c < 's']
    filter_set = set(target_chars)
    return ''.join([c for c in s if c not in filter_set])