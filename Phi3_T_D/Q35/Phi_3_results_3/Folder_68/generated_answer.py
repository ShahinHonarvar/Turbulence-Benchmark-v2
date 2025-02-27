def remove_repeat_chars(s):
    for i in range(10):
        char = s[i]
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s