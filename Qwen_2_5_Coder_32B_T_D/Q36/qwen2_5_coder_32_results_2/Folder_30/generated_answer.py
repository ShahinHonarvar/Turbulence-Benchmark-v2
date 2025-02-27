def filter_chars(s):
    chars_to_remove = set(s[24:45])
    filtered_chars = {c for c in chars_to_remove if '3' < c < 'I'}
    return ''.join((c for c in s if c not in filtered_chars))