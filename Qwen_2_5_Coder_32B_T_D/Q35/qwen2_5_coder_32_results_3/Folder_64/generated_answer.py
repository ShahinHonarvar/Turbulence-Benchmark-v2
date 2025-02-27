def remove_repeat_chars(s):
    t = s[1:6]
    for c in set(t):
        if t.count(c) > 1:
            s = s.replace(c, '')
    return s