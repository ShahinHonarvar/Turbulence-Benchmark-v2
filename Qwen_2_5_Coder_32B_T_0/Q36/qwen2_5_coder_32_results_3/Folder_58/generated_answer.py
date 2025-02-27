def filter_chars(s):
    chars_to_remove = set(s[318:337])
    filtered_chars = {c for c in chars_to_remove if 'B' < c < 'z'}
    return ''.join((c for c in s if c not in filtered_chars))