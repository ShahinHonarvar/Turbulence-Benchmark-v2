def filter_chars(s):
    chars = set(s[33:71]) & set('789:;<=>?@abcd')
    return ''.join((c for c in s if c not in chars))