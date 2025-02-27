def filter_chars(s):
    chars_to_remove = set('6789AB')
    return ''.join((c for i, c in enumerate(s) if i < 138 or i > 920 or c not in chars_to_remove))