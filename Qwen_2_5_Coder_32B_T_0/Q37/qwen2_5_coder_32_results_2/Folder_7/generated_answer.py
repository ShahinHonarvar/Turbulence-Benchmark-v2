def filter_chars(s):
    if len(s) < 723:
        return s
    chars_to_remove = set(s[521:723]) & set('><=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\\]^_')
    return ''.join((c for c in s if c not in chars_to_remove))