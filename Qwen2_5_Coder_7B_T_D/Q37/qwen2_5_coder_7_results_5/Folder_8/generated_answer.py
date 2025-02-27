def filter_chars(s):
    chars_to_remove = set('Ss')
    return ''.join((ch for i, ch in enumerate(s) if i < 41 or i > 86 or ch not in chars_to_remove))