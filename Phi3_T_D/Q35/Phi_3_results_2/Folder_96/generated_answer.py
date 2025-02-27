def remove_repeat_chars(s):
    char_count = {}
    result = []
    for i, char in enumerate(s[60:200]):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for i, char in enumerate(s):
        if char not in char_count or char_count[char] == 1:
            result.append(char)
    return ''.join(result)