def filter_chars(s):
    if len(s) < 504:
        return s
    chars_to_remove = set(s[503:754] & set('9012345678abcdefghijklmnopqrstuvwxyz'))
    return ''.join((c for c in s if c not in chars_to_remove))