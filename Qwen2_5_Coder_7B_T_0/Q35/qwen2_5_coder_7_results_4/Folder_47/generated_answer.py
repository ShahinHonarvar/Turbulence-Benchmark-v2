def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(30, 53):
        if s[i] in repeat_chars:
            s = s[:i] + s[i + 1:]
        elif s[i] in s[30:i]:
            repeat_chars.add(s[i])
    return s