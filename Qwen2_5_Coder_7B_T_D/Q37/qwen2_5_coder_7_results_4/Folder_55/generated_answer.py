def filter_chars(s):
    chars_to_remove = set(';$')
    return ''.join((c for i, c in enumerate(s) if i not in range(1, 6) or c not in chars_to_remove))