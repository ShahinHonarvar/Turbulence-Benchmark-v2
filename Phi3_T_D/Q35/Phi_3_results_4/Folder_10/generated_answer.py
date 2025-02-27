def remove_repeat_chars(s):
    char_count = {}
    for i in range(36 + 1, 54):
        if s[i] in char_count:
            char_count[s[i]] += 1
            if char_count[s[i]] > 1:
                s = s.replace(s[i], '', s.count(s[i]))
        else:
            char_count[s[i]] = 1
    return s