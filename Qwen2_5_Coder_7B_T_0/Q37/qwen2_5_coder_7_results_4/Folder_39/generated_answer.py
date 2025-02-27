def filter_chars(s):
    chars_to_remove = set('ABCDEF')
    return ''.join((c for i, c in enumerate(s) if i < 52 or i > 81 or c not in chars_to_remove))