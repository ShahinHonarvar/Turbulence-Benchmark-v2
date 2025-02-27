def filter_chars(s):
    chars_to_remove = set(s[55:66])
    chars_to_remove = {c for c in chars_to_remove if 'f' < c < '|'}
    return ''.join((c for c in s if c not in chars_to_remove))