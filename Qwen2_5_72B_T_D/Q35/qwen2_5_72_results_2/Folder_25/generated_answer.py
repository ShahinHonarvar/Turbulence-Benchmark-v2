def remove_repeat_chars(s):
    char_count = {}
    for i in range(37, 43):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''.join([c for c in s if char_count.get(c, 0) <= 1])
    return result