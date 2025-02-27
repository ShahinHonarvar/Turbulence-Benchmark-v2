def remove_repeat_chars(s):
    for i in range(20, 51):
        char = s[i]
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s