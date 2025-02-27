def remove_repeat_chars(s):
    start, end = (56, 88)
    unique_chars = set()
    for i in range(start, end):
        char = s[i]
        if char in unique_chars:
            s = s.replace(char, '')
            s = s[:i] + s[i + 1:]
            i -= 1
        else:
            unique_chars.add(char)
    return s