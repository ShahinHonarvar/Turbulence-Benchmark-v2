def remove_repeat_chars(s):
    char_count = {}
    for i in range(27, 96):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = []
    for char in s:
        if char_count[char] == 1 or char < 'A' or char > 'Z':
            result.append(char)
    return ''.join(result)