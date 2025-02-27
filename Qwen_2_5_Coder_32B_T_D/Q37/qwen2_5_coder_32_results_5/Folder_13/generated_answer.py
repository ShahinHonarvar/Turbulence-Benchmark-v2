def filter_chars(s):
    if len(s) <= 854:
        return s
    chars_to_remove = set(s[124:855] & set('90123456789:;<=>?@abcdefghijklmnopqrstuvwxyz'))
    return ''.join((c for c in s if c not in chars_to_remove))