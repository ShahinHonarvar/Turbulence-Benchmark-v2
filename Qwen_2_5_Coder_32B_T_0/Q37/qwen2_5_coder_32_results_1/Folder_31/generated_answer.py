def filter_chars(s):
    chars_to_remove = set(s[57:97]) & set('<>[]^_`abcdefghijklmnopqrstuvwxyz')
    return ''.join((c for c in s if c not in chars_to_remove))