def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(61, 200):
        if s[i] in repeat_chars:
            s = s[:i] + s[i + 1:]
        elif s[i] in s[61:i]:
            repeat_chars.add(s[i])
    return s