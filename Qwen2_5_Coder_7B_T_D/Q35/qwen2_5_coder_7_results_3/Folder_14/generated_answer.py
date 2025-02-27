def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(2, 5):
        if s[i] in repeat_chars:
            s = s.replace(s[i], '', s.count(s[i]))
        else:
            repeat_chars.add(s[i])
    return s