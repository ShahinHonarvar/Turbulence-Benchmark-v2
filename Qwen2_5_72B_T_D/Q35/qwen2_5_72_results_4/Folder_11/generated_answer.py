def remove_repeat_chars(s):
    char_count = {}
    for i in range(48, 76):
        char_count[chr(i)] = 0
    for char in s:
        if char in char_count:
            char_count[char] += 1
    result = ''
    for char in s:
        if char not in char_count or char_count[char] == 1:
            result += char
    return result