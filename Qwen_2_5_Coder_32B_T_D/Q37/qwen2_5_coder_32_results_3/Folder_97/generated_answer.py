def filter_chars(s):
    chars_to_remove = set(s[227:236])
    filtered_chars = {c for c in chars_to_remove if 'D' <= c <= 'u'}
    return ''.join((c for c in s if c not in filtered_chars))