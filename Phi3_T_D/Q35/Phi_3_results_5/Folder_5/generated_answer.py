def remove_repeat_chars(s):
    char_set = set()
    for i in range(3, 9):
        if s[i] in char_set:
            s = s.replace(s[i], '')
        else:
            char_set.add(s[i])
    return s