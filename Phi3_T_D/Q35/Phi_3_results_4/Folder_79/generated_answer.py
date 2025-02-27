def remove_repeat_chars(s):
    for i in range(2, 8):
        s = s.replace(s[i - 1], '')
    return s