def remove_repeat_chars(s):
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    for c, count in char_count.items():
        if count > 1 and 34 < s.index(c) < 69:
            s = s.replace(c, '')
    return s