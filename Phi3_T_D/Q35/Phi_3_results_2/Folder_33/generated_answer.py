def remove_repeat_chars(s):
    start, end = (125, 825)
    seen_chars = {}
    for i in range(start, end):
        char = s[i]
        if char in seen_chars:
            s = s.replace(char, '', 1)
        else:
            seen_chars[char] = s[i]
    return s