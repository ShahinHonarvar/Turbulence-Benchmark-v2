def remove_repeat_chars(s):
    s = list(s)
    for i, c in enumerate(s[37:43]):
        if s[37:43].count(c) > 1:
            s.remove(c)
    return ''.join(s)