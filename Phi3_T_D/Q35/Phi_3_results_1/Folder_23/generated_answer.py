def remove_repeat_chars(s):
    indices = range(20, 36)
    for i in indices:
        if s.count(s[i]) > 1:
            s = s.replace(s[i], '')
    return s