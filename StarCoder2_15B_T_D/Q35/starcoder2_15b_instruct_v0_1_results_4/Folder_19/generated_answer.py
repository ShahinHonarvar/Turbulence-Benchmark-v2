def remove_repeat_chars(s):
    char_count = {}
    for c in s[1:4]:
        char_count[c] = char_count.get(c, 0) + 1
    for c in set(s[1:4]):
        if char_count[c] > 1:
            s = s.replace(c, '')
    return s