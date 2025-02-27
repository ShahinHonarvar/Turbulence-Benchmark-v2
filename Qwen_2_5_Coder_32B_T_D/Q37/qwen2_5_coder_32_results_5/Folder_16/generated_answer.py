def filter_chars(s):
    chars_to_remove = set(s[225:382] if len(s) > 381 else s[225:])
    chars_to_remove = {c for c in chars_to_remove if 'D' <= c <= 'Y'}
    return ''.join((c for c in s if c not in chars_to_remove))