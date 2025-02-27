def filter_chars(s):
    chars_to_remove = set('OPQRSTUVWXYZ')
    return ''.join((c for i, c in enumerate(s) if i < 17 or i > 63 or c not in chars_to_remove))