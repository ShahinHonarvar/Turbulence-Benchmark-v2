def remove_repeat_chars(s):
    start, end = (103, 802)
    char_map = {}
    for i in range(start, end):
        char = s[i]
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    altered_s = ''.join([char for char in s if char_map[char] <= 1 or s.index(char) < start or s.index(char) >= end])
    return altered_s