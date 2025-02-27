def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, 7):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [s[0]]
    for i in range(1, 7):
        char = s[i]
        if char_count[char] > 1:
            continue
        result.append(char)
    for i in range(8, len(s)):
        result.append(s[i])
    return ''.join(result)