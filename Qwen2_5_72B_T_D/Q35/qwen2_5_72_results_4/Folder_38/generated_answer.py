def remove_repeat_chars(s):
    char_count = {}
    for i in range(37, 85):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = []
    for char in s:
        if char_count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)