def remove_repeat_chars(s):
    return ''.join((c for i, c in enumerate(s) if i not in range(1, 8) or s.index(c) == i))