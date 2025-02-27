def remove_repeat_chars(s):
    chars_to_remove = set(s[13:91])
    return ''.join((c for i, c in enumerate(s) if (i < 13 or i >= 91) or c not in chars_to_remove))