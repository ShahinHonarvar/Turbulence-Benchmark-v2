def filter_chars(s):
    filter_set = set(range(155, 404))
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()[]{};:,.<>?')
    return ''.join((c for i, c in enumerate(s) if i not in filter_set or c in valid_chars))