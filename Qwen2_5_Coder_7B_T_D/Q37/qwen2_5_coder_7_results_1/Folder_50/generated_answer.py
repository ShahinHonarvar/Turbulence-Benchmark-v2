def filter_chars(s):
    chars_to_remove = set(range(ord('_'), ord('o') + 1))
    return ''.join((c for c in s if ord(c) < 71 or ord(c) > 96 or c not in chars_to_remove))