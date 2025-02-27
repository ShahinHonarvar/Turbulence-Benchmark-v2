def filter_chars(s):
    chars_to_remove = set(s[40:63])
    chars_to_remove = {c for c in chars_to_remove if '7' < c < 'H'}
    return ''.join((c for c in s if c not in chars_to_remove))