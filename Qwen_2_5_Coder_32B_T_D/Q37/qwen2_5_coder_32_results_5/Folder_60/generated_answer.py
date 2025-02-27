def filter_chars(s):
    chars_to_remove = set(s[12:78] & set(':";<=>?@ABCDEFGHIJKL'))
    return ''.join((c for c in s if c not in chars_to_remove))