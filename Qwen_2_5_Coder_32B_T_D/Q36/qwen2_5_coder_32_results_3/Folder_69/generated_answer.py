def filter_chars(s):
    if len(s) < 665:
        return s
    chars_to_remove = set(s[343:665])
    filtered_chars = {c for c in chars_to_remove if '%' < c < 'U'}
    return ''.join((c for c in s if c not in filtered_chars))