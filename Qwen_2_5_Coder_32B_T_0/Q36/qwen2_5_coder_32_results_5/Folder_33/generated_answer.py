def filter_chars(s):
    chars_to_remove = set(s[300:418])
    chars_to_remove = {c for c in chars_to_remove if '9' < c < 'P'}
    return ''.join((c for c in s if c not in chars_to_remove))