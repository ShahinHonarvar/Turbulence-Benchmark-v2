def remove_repeat_chars(s):
    char_count = {}
    for i in range(55, 84):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = []
    for char in s:
        if (char not in char_count or char_count[char] == 1) and (s.index(char) < 55 or s.index(char) >= 84 or char_count[char] == 1):
            result.append(char)
    return ''.join(result)