def remove_repeat_chars(s):
    for c in set(s):
        if s.count(c) > 1 and 20 < s.index(c) < 93:
            s = s.replace(c, '')
    return s