def filter_chars(s):
    chars_to_remove = set(s[10:70]) & set('IJK')
    return ''.join((c for c in s if c not in chars_to_remove))