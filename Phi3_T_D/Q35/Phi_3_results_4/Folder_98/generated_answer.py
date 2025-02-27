def remove_repeat_chars(s):
    for i in range(6):
        if i < len(s) and s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
    return s