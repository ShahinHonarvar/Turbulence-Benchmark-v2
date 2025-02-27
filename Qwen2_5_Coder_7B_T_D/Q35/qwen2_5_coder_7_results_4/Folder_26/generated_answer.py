def remove_repeat_chars(s):
    char_count = {}
    for i in range(68, 99):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = []
    for char in s:
        if (char not in char_count or char_count[char] == 1) or (char_count[char] > 1 and s.index(char) < 68 or s.rindex(char) >= 99):
            result.append(char)
    return ''.join(result)