def remove_repeat_chars(s):
    for i in range(87, 99):
        c = s[i]
        s = s.replace(c, '', s[i + 1:].count(c))
    return s