def filter_chars(s):
    chars_to_remove = set(s[43:59])
    filtered_chars = {c for c in chars_to_remove if '5' < c < 'C'}
    return ''.join((c for c in s if c not in filtered_chars))