def filter_chars(s):
    chars_to_remove = set(s[19:34]) & set('S{TUVWXYZ[]\\\\^_`')
    return ''.join((c for c in s if c not in chars_to_remove))