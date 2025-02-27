def remove_repeat_chars(s):
    target_chars = set()
    new_s = []
    for i, c in enumerate(s[81:86]):
        if c in target_chars or s.count(c, i, i + 6) > 1:
            target_chars.add(c)
        else:
            new_s.append(c)
    return ''.join(new_s)