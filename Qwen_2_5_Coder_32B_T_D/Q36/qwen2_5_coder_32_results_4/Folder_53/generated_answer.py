def filter_chars(s):
    if len(s) <= 98:
        return s
    chars_to_remove = set(s[91:97])
    chars_to_remove = {c for c in chars_to_remove if 'j' < c < 'w'}
    return ''.join((c for c in s if c not in chars_to_remove))