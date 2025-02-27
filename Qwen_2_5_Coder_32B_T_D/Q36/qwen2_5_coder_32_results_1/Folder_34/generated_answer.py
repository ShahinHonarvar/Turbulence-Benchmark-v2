def filter_chars(s):
    chars_to_remove = set(s[11:79])
    filtered_chars = {c for c in chars_to_remove if '?' < c < 'm'}
    return ''.join((c for c in s if c not in filtered_chars))