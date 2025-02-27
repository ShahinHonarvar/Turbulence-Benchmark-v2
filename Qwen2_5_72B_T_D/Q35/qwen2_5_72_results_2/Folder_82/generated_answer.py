def remove_repeat_chars(s):
    char_count = {}
    for i in range(30, 200):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = []
    for i, char in enumerate(s):
        if i < 30 or i >= 200 or char_count.get(char, 0) == 1:
            result.append(char)
    return ''.join(result)