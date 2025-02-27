def filter_chars(s):
    if len(s) < 539:
        return s
    chars_to_remove = set(s[515:539]) & set('+-*/0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}')
    return ''.join((c for c in s if c not in chars_to_remove))