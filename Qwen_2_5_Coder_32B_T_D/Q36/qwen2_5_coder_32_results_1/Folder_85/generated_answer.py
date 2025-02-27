def filter_chars(s):
    chars_to_remove = set(s[55:80])
    filtered_chars = {c for c in chars_to_remove if 'S' < c < 's'}
    return ''.join((c for c in s if c not in filtered_chars))