def remove_repeat_chars(s):
    seen = set()
    for i in range(30, 200):
        char = s[i]
        if char in seen:
            s = s.replace(char, '')
            continue
        seen.add(char)
    return s