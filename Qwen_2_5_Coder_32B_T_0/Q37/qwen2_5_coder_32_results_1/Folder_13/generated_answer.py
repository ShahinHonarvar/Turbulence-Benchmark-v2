def filter_chars(s):
    if len(s) < 855:
        return s
    chars_to_remove = set(s[124:855])
    chars_to_remove = {c for c in chars_to_remove if '9' <= c <= 's'}
    return ''.join((c for c in s if c not in chars_to_remove))