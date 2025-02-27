def filter_chars(s):
    if len(s) < 90:
        return s
    chars_to_remove = set(s[35:90].intersection('EFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))
    return ''.join((c for c in s if c not in chars_to_remove))