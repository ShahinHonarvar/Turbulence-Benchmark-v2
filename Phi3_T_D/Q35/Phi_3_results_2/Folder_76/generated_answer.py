def remove_repeat_chars(s):
    char_count = {}
    for i in range(330, 543):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    return ''.join([c for i, c in enumerate(s) if (i < 330 or i >= 543) or char_count[c] == 1])