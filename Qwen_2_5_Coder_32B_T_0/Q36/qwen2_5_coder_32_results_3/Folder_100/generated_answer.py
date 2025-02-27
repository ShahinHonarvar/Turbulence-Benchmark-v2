def filter_chars(s):
    chars_to_remove = set(s[43:69])
    chars_to_remove = {c for c in chars_to_remove if 'B' < c < 'r'}
    return ''.join((c for c in s if c not in chars_to_remove))