def filter_chars(s):
    chars_to_remove = set(s[44:59]) & set('012345')
    return ''.join((c for c in s if c not in chars_to_remove))