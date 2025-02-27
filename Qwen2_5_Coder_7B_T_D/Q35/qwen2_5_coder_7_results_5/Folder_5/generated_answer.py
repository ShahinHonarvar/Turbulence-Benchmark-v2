def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(2, 8):
        if s[i] in repeat_chars:
            s = s.replace(s[i], '')
        elif s[i] in s[2:8]:
            repeat_chars.add(s[i])
    return s