def remove_repeat_chars(s):
    indices = range(77, 84)
    char_count = {}
    for i in indices:
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = list(s)
    for i in indices:
        if char_count[s[i]] > 1:
            result[i] = ''
    return ''.join(result)