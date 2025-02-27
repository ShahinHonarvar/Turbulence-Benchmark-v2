def filter_chars(s):
    chars_to_remove = set('!@#$%^&*()_+=-[]{}|;:,.<>?')
    return ''.join((c for i, c in enumerate(s) if i not in range(27, 86) or c not in chars_to_remove))