def filter_chars(s):
    filter_set = set('&' + 'abcdefghijklmnopqrstuvwxyz'[:18])
    return ''.join((c for c in s if c not in filter_set))