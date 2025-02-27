def remove_repeat_chars(s):
    modified_chars = []
    char_count = {}
    for i in range(91, 199):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
            if char_count[char] > 2:
                continue
        else:
            char_count[char] = 1
        if char_count[char] == 1:
            modified_chars.append(char)
    return ''.join(modified_chars)