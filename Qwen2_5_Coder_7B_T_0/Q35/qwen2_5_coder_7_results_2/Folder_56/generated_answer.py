def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(7, 9):
        if s[i] in repeat_chars:
            s = s[:i] + s[i + 1:]
        else:
            repeat_chars.add(s[i])
    return s