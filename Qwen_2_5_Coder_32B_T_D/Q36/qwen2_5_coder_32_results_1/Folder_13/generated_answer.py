def filter_chars(s):
    if len(s) < 527:
        return s
    chars_to_remove = set(s[324:526])
    chars_to_remove = {c for c in chars_to_remove if ')' < c < 'O'}
    return ''.join((c for c in s if c not in chars_to_remove))