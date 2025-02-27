def filter_chars(s):
    if len(s) < 93:
        return s
    chars_to_remove = set(s[42:93])
    chars_to_remove = {c for c in chars_to_remove if '/' <= c <= 'a'}
    return ''.join((c for c in s if c not in chars_to_remove))