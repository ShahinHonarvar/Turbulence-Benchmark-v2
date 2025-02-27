def remove_repeat_chars(s):
    unique_chars = set()
    for i in range(42, 87):
        char = s[i]
        if char in unique_chars:
            s = s.replace(char, '', 1)
        else:
            unique_chars.add(char)
    return s