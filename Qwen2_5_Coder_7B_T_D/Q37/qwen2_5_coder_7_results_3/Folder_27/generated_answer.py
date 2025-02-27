def filter_chars(s):
    chars_to_remove = set('=ABCDE')
    return ''.join((c for i, c in enumerate(s) if i < 43 or i > 80 or c not in chars_to_remove))