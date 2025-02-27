def remove_repeat_chars(s):
    chars_to_remove = set(s[2:5])
    return ''.join((c for i, c in enumerate(s) if i < 2 or i > 4 or c not in chars_to_remove))