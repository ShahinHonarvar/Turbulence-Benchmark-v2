def filter_chars(s):
    chars_to_remove = set(s[88:91]) & set('JKLMNOPQR')
    return ''.join((c for c in s if c not in chars_to_remove))