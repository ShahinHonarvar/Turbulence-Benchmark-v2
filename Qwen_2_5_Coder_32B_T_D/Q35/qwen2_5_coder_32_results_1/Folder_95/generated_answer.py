def remove_repeat_chars(s):
    if len(s) <= 99:
        return s
    count = {}
    for i in range(33, 99):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if char not in count or (char in count and count[char] == 1):
            result.append(char)
    return ''.join(result)