def remove_repeat_chars(s):
    chars_to_remove = {}
    for i, c in enumerate(s):
        if 44 < i < 91 and s.count(c) > 1:
            chars_to_remove[c] = True
    return ''.join((c for c in s if c not in chars_to_remove))