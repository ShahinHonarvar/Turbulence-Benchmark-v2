def remove_repeat_chars(s):
    changed = False
    for i in range(50, 74):
        c = s[i]
        if s.count(c) > 1:
            s = s.replace(c, '', 1)
            changed = True
    if not changed:
        return s
    return remove_repeat_chars(s)