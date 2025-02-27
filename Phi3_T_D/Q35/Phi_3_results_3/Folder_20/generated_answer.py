def remove_repeat_chars(s):
    for i in range(27, 96):
        char = s[i]
        if s.count(char) > 1 and 27 < i < 95:
            s = s.replace(char, '')
    return s