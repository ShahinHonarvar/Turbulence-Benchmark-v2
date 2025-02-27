def filter_chars(s):
    chars_to_remove = set('STUVWXYZ')
    return ''.join((c for i, c in enumerate(s) if i < 19 or i > 33 or c not in chars_to_remove))