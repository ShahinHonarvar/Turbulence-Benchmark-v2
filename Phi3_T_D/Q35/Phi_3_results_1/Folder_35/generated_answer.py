def remove_repeat_chars(s):
    chars = [c for i, c in enumerate(s) if 77 < i < 84 and s.count(c) > 1]
    for char in chars:
        s = s.replace(char, '')
    return s