def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(2, 8):
        if s[i] in repeat_chars:
            s = s[:i] + s[i + 1:]
        elif s[i] in s[2:i] + s[i + 1:]:
            repeat_chars.add(s[i])
    return s