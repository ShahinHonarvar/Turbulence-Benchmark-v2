def filter_chars(s):
    chars_to_remove = set(';$')
    return ''.join((c for i, c in enumerate(s) if i < 2 or i > 5 or c not in chars_to_remove))