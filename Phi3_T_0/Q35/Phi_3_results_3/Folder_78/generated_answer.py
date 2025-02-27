def remove_repeat_chars(s):
    char_count = {}
    for i in range(62, 96):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [char for char in s if char not in char_count or char_count[char] == 1]
    return ''.join(result)