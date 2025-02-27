def remove_repeat_chars(s):
    char_count = {}
    for i in range(18, 60):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = []
    for i, char in enumerate(s):
        if i < 18 or i >= 60 or char_count.get(char, 0) < 2:
            result.append(char)
    return ''.join(result)