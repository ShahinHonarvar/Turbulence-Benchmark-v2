def filter_chars(s):
    chars_to_remove = set(s[54:92])
    chars_to_remove = {c for c in chars_to_remove if 'J' < c < 'X'}
    return ''.join((c for c in s if c not in chars_to_remove))