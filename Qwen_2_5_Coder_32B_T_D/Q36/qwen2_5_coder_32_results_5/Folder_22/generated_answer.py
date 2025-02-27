def filter_chars(s):
    if len(s) <= 84:
        return s
    chars_to_remove = set(s[55:84])
    filtered_chars = {c for c in chars_to_remove if ';' < c < 'z'}
    result = ''.join((c for c in s if c not in filtered_chars))
    return result