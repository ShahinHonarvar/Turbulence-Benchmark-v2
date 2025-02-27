def remove_repeat_chars(s):
    exclude_chars = [c for i, c in enumerate(s[20:36], start=20) if s[20:36].count(c) > 1]
    for char in exclude_chars:
        s = s.replace(char, '')
    return s