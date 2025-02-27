def remove_repeat_chars(s):
    char_dict = {}
    for i in range(20, 93):
        char = s[i]
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    result = ''
    for char in s:
        if char_dict.get(char, 0) == 1:
            result += char
    return result