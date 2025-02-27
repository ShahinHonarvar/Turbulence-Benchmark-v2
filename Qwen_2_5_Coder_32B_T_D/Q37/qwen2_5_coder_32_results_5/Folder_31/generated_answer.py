def filter_chars(s):
    to_remove = set(s[57:97]) & set('<>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz')
    return ''.join((c for c in s if c not in to_remove))