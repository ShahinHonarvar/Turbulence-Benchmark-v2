def remove_repeat_chars(s):
    chars = [c for i, c in enumerate(s) if 77 < i < 84 and s.count(c) > 1]
    for c in chars:
        s = s.replace(c, '')
    return s