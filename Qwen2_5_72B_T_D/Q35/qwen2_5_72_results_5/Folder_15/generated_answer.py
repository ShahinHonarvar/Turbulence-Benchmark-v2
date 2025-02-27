def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, 4):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''.join([ch for ch in s if char_count.get(ch, 0) < 2])
    return result