def filter_chars(s):
    chars_to_remove = set(s[2:7])
    chars_to_remove = {c for c in chars_to_remove if 'h' < c < 'k'}
    return ''.join((c for c in s if c not in chars_to_remove))