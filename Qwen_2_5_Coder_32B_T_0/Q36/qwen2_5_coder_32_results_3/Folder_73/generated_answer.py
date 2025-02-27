def filter_chars(s):
    chars_to_remove = set(s[66:90])
    filtered_chars = {c for c in chars_to_remove if '#' < c < 'T'}
    return ''.join((c for c in s if c not in filtered_chars))