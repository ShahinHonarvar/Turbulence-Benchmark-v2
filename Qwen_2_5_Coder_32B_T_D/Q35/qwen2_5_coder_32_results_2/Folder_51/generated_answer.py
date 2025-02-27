def remove_repeat_chars(s):
    t = s[7:9]
    for char in set(t):
        if t.count(char) > 1:
            s = s.replace(char, '')
    return s