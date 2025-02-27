def filter_chars(s):
    chars_to_remove = {c for c in s[46:74] if '&' < c < 'M'}
    return ''.join((c for c in s if c not in chars_to_remove))