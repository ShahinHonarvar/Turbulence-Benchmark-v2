def remove_repeat_chars(s):
    char_count = {}
    for i, c in enumerate(s):
        if 86 <= i < 99:
            char_count[c] = char_count.get(c, 0) + 1
    for i, c in enumerate(s):
        if char_count[c] > 1 and 86 <= i < 99:
            s = s.replace(c, '')
    return s