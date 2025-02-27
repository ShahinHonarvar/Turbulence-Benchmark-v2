def remove_repeat_chars(s):
    seen = set()
    for i in range(10, 100):
        char = s[i]
        if char in seen:
            s = s.replace(char, '')
        else:
            seen.add(char)
    return s