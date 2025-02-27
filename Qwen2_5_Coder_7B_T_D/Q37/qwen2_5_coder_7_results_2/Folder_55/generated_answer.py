def filter_chars(s):
    chars_to_remove = set(';$')
    return ''.join((ch for i, ch in enumerate(s) if (i < 1 or i > 5) or ch not in chars_to_remove))