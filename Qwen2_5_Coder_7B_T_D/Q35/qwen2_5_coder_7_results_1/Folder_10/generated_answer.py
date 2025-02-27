def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(36, 54):
        if s[i] in repeat_chars:
            s = s[:i] + s[i + 1:]
        elif s[i] in s[36:i] + s[i + 1:54]:
            repeat_chars.add(s[i])
    return s