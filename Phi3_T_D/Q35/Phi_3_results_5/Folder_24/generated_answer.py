def remove_repeat_chars(s):
    if len(s) < 13:
        return s
    for i in range(13, 90):
        if s.count(s[i]) > 1:
            s = s.replace(s[i], '')
    return s