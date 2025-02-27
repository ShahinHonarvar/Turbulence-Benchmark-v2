def remove_repeat_chars(s):
    if not s or len(s) < 20:
        return s
    char_count = {}
    for i in range(13, 91):
        if s[i] in char_count:
            char_count[s[i]] += 1
            s = s.replace(s[i], '', 1)
        else:
            char_count[s[i]] = 1
    return s