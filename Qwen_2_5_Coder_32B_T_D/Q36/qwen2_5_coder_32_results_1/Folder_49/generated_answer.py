def filter_chars(s):
    chars_to_remove = set(s[47:91]) & set('EFG')
    return ''.join((c for c in s if c not in chars_to_remove))