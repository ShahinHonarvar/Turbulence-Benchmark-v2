def filter_chars(s):
    to_remove = set(s[521:723]) & set('>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_')
    return ''.join((c for c in s if c not in to_remove))