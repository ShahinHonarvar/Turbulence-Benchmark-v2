def remove_repeat_chars(s):
    target_range = s[20:43]
    char_count = {}
    for char in target_range:
        char_count[char] = char_count.get(char, 0) + 1
    for char in char_count:
        if char_count[char] > 1:
            s = s.replace(char, '')
    return s