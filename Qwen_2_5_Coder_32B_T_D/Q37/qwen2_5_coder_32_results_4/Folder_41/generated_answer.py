def filter_chars(s):
    char_set = set(s[26:65])
    filter_set = {c for c in char_set if 'V' <= c <= 'o'}
    return ''.join((c for c in s if c not in filter_set))