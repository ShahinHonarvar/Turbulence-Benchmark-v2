def filter_chars(s):
    chars_to_remove = set(s[78:87])
    filtered_chars = {c for c in chars_to_remove if ';' < c < 'r'}
    return ''.join((c for c in s if c not in filtered_chars))