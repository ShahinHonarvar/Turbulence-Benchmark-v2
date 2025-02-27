def filter_chars(s):
    chars_to_remove = set(s[71:74])
    filtered_chars = {c for c in chars_to_remove if 'A' < c < 'U'}
    return ''.join((c for c in s if c not in filtered_chars))