def remove_repeat_chars(s):
    for i in range(1, 8):
        s = s.replace(s[i], '')
    return s