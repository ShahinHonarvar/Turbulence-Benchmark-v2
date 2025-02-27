def filter_chars(s):
    chars_to_remove = set('abcdefghi')
    return ''.join((c for i, c in enumerate(s) if i < 36 or i > 79 or c not in chars_to_remove))