def filter_chars(s):
    chars_to_remove = set(s[4:8])
    chars_to_remove = {c for c in chars_to_remove if '1' < c < 'J'}
    return ''.join((c for c in s if c not in chars_to_remove))