def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(21, 200):
        if s[i] in repeat_chars:
            s = s[:i] + s[i + 1:]
        else:
            count = s.count(s[i], 21, 200)
            if count > 1:
                repeat_chars.add(s[i])
    return s