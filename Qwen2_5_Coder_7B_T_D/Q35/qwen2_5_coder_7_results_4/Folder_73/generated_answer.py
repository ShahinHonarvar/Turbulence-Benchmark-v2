def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(10, 76):
        if s[i] in s[10:76] and s[i] not in repeat_chars:
            repeat_chars.add(s[i])
    for char in repeat_chars:
        s = s.replace(char, '')
    return s