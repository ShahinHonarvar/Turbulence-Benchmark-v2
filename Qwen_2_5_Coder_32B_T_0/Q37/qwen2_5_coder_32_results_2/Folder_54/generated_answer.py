def filter_chars(s):
    chars_to_remove = set(s[46:86] & set('-X'))
    return ''.join((c for c in s if c not in chars_to_remove))