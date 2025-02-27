def remove_repeat_chars(s):
    char_count = {}
    for i in range(44, 78):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    new_s = ''.join([char for char in s if char not in char_count or char_count[char] == 1])
    return new_s