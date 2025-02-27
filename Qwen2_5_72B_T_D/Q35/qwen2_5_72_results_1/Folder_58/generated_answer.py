def remove_repeat_chars(s):
    char_count = {}
    for i in range(103, 802):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = []
    for i, char in enumerate(s):
        if i < 103 or i >= 802 or char_count.get(char, 0) < 2:
            result.append(char)
    return ''.join(result)