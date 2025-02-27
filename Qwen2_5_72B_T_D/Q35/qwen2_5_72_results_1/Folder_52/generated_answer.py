def remove_repeat_chars(s):
    char_count = {}
    for i in range(38, 81):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''
    for char in s:
        if char_count.get(char, 1) == 1:
            result += char
    return result