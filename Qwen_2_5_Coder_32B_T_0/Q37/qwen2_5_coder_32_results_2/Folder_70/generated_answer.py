def filter_chars(s):
    chars_to_remove = set(s[515:539]) & set('+}')[::-1]
    return ''.join((c for c in s if c not in chars_to_remove))