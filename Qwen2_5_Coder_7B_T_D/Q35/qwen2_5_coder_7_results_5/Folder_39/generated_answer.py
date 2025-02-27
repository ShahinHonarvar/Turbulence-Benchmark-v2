def remove_repeat_chars(s):
    char_count = {}
    for i in range(44, 91):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = []
    for char in s:
        if char_count[char] < 2 or not (44 < s.find(char) < 91 and s.count(char) > 1):
            result.append(char)
    return ''.join(result)