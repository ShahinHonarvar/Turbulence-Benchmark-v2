def filter_chars(s):
    chars_to_remove = set(s[50:56] if len(s) > 56 else s[50:])
    chars_to_remove = {c for c in chars_to_remove if 'I' < c < 'a'}
    return ''.join((c for c in s if c not in chars_to_remove))