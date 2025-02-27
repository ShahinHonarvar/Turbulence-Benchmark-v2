def remove_repeat_chars(s):
    return ''.join((c for i, c in enumerate(s) if 3 < i < 8 and s.count(c, 3, 8) == 1))