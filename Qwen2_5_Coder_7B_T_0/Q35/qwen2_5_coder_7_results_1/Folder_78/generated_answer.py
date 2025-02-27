def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(62, 96):
        if s[i] in repeat_chars:
            s = s[:i] + s[i + 1:]
        elif s[i] in s[62:i]:
            repeat_chars.add(s[i])
    return s