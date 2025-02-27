def remove_repeat_chars(s):
    char_count = {}
    for i in range(6, 9):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''.join([c for c in s if char_count.get(c, 0) < 2])
    return result