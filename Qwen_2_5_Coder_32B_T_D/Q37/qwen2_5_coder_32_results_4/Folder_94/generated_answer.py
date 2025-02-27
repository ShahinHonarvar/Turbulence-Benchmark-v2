def filter_chars(s):
    chars_to_remove = set(s[51:97] & set('Xp'))
    return ''.join((c for c in s if c not in chars_to_remove))