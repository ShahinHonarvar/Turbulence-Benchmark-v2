def remove_repeat_chars(s):
    indices = range(125, 825)
    for i in indices:
        if s.count(s[i]) > 1 and i in indices:
            s = s[0:i] + s[i + 1:]
    return s