def remove_repeat_chars(s):
    char_count = {}
    new_s = ''
    for i in range(58, 84):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    for i in range(len(s)):
        if i < 58 or i > 83 or char_count[s[i]] < 2:
            new_s += s[i]
    return new_s