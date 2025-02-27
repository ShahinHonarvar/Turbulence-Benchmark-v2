def remove_repeat_chars(s):
    char_count = {}
    result = []
    for i in range(355, 988):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    for char in s:
        if char not in char_count or char_count[char] == 1:
            result.append(char)
    return ''.join(result)