def remove_repeat_chars(s):
    return ''.join((c for i, c in enumerate(s) if s.count(c, 0, i) < 2))