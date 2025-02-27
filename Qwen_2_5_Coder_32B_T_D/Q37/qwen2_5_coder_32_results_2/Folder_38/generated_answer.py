def filter_chars(s):
    target_chars = set(s[24:80])
    chars_to_remove = {c for c in target_chars if 'a' <= c <= 'f'}
    return ''.join((c for c in s if c not in chars_to_remove))