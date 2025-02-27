def filter_chars(s):
    chars_to_remove = set(s[56:86])
    valid_chars = {c for c in chars_to_remove if '+' < c < 'w'}
    return ''.join((c for c in s if c not in valid_chars))