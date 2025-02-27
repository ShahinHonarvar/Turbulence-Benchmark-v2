def remove_repeat_chars(s):
    pos = (34, 69)
    for i in range(pos[0], pos[1]):
        if s[i] in s[pos[0]:pos[1]] and s.count(s[i]) > 1:
            s = s.replace(s[i], '')
    return s