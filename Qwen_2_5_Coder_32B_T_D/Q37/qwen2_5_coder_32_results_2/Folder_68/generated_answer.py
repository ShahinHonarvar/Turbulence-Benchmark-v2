def filter_chars(s):
    chars_to_remove = set(s[7:10])
    filtered_chars = {c for c in chars_to_remove if '6' <= c <= 'w'}
    return ''.join((c for c in s if c not in filtered_chars))