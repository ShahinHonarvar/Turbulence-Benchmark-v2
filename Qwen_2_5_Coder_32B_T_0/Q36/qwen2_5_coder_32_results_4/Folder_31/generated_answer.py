def filter_chars(s):
    chars_to_remove = set(s[14:75])
    chars_to_remove = {c for c in chars_to_remove if '9' < c < 'K'}
    return ''.join((c for c in s if c not in chars_to_remove))