def remove_repeat_chars(s):
    return ''.join([x for i, x in enumerate(s) if i not in range(22, 24) or s.count(x, i + 1) == 0])