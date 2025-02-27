def filter_chars(s):
    chars_to_remove = {c for c in s[78:81] if 'S' < c < '['}
    return ''.join((c for c in s if c not in chars_to_remove))