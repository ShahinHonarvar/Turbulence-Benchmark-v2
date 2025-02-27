def filter_chars(s):
    chars_to_remove = set('DEFGHIJKLMNPQRSTUVWXYZ')
    return ''.join((c for i, c in enumerate(s) if i < 227 or i > 235 or c not in chars_to_remove))