def remove_repeat_chars(s):
    indices = list(range(68, 99))
    char_count = {}
    for i in indices:
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = []
    for char in s:
        if (char not in char_count or char_count[char] == 1) or s.index(char) not in indices:
            result.append(char)
    return ''.join(result)