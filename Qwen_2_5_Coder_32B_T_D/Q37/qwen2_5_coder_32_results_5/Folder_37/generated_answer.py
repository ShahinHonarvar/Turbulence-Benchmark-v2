def filter_chars(s):
    chars_to_remove = set(s[17:64] & set('OPQRSTUVWXYZ[^_'))
    return ''.join((c for c in s if c not in chars_to_remove))