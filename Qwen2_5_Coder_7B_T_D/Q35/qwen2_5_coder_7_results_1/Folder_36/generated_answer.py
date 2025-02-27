def remove_repeat_chars(s):
    indices = list(range(477, 709))
    char_count = {}
    for i in indices:
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if char_count[s[i]] == 1 or i not in indices:
            result += s[i]
    return result