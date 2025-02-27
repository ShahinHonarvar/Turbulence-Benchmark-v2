def remove_repeat_chars(s):
    char_count = {}
    for i in range(20, 36):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    modified_s = ''.join([c for i, c in enumerate(s) if c not in char_count or char_count[c] == 1])
    return modified_s