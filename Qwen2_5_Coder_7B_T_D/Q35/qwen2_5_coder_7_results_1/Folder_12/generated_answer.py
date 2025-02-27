def remove_repeat_chars(input_str):
    char_count = {}
    for i in range(17, 87):
        char = input_str[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = []
    for i in range(len(input_str)):
        char = input_str[i]
        if (i < 17 or i >= 87) or char_count[char] == 1:
            result.append(char)
    return ''.join(result)