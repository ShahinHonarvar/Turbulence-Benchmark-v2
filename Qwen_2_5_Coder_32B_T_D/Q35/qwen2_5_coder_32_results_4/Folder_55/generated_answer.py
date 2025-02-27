def remove_repeat_chars(s):
    if len(s) <= 100:
        return s
    count = {}
    for i in range(11, 100):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = []
    for i, char in enumerate(s):
        if i < 11 or i >= 100 or count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)