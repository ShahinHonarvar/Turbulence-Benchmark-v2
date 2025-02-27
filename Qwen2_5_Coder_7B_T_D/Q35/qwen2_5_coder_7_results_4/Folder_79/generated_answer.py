def remove_repeat_chars(s):
    return ''.join((ch for i, ch in enumerate(s) if i not in range(1, 8) or s.count(ch) == 1))