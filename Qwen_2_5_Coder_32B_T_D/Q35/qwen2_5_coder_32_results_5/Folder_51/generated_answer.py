def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    target = s[7:9]
    char_count = {}
    for char in target:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in char_count:
        if char_count[char] > 1:
            s = s.replace(char, '')
    return s