def remove_repeat_chars(s):
    if len(s) <= 93:
        return s
    count = {}
    for i in range(21, 93):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if char not in count or count[char] == 1:
            result.append(char)
    return ''.join(result)