def remove_repeat_chars(s):
    if len(s) <= 802:
        return s
    count = {}
    for i in range(104, 802):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = []
    for char in s:
        if count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)