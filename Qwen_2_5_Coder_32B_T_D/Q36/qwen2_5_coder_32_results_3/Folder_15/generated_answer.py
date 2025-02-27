def filter_chars(s):
    chars_to_remove = set(s[2:7]) & set('ijk')
    return ''.join((c for c in s if c not in chars_to_remove))