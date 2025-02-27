def filter_chars(s):
    chars_to_remove = set('!@#$%^&*()_+{}|:"<>?')
    return ''.join((c for i, c in enumerate(s) if i < 27 or i > 85 or c not in chars_to_remove))