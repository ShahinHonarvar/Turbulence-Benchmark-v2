def filter_chars(s):
    if len(s) < 419:
        return s
    chars_to_remove = set(s[300:418])
    filtered_chars = {c for c in chars_to_remove if '9' < c < 'P'}
    return ''.join((c for c in s if c not in filtered_chars))