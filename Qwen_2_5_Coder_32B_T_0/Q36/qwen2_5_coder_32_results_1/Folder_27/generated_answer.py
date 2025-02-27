def filter_chars(s):
    chars_to_remove = set(s[48:75])
    chars_to_remove = {c for c in chars_to_remove if '6' < c < '_'}
    return ''.join((c for c in s if c not in chars_to_remove))