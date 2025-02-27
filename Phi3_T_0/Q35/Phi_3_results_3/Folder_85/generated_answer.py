def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, 8):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [s[0]]
    for i in range(1, 8):
        char = s[i]
        if char_count[char] > 1:
            continue
        result.append(char)
    result.extend(s[8:])
    return ''.join(result)