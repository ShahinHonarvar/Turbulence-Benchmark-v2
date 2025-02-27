def filter_chars(s):
    if len(s) < 855:
        return s
    chars_to_remove = set(s[124:855]) & set('9012345678abcdefghijklmnopqrst')
    return ''.join((c for c in s if c not in chars_to_remove))