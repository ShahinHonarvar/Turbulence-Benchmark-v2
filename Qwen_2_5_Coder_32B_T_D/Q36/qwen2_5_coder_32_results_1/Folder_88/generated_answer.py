def filter_chars(s):
    if len(s) < 82:
        return s
    chars_to_remove = set(s[79:81])
    chars_to_remove = {c for c in chars_to_remove if 'S' < c < '['}
    return ''.join((c for c in s if c not in chars_to_remove))