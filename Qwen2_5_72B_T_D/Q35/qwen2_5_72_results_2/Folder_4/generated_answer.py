def remove_repeat_chars(s):
    char_count = {}
    for i in range(49, 74):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = []
    for char in s:
        if char not in char_count or char_count[char] == 1:
            result.append(char)
    return ''.join(result)