def remove_repeat_chars(s):
    char_count = {}
    for i in range(58, 84):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = []
    for i in range(len(s)):
        char = s[i]
        if (i < 57 or i >= 84) or char_count[char] == 1:
            result.append(char)
    return ''.join(result)