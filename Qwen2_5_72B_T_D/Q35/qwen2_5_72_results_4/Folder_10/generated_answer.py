def remove_repeat_chars(s):
    char_count = {}
    for i in range(36, 54):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''.join([c for c in s if c not in char_count or char_count[c] == 1])
    return result