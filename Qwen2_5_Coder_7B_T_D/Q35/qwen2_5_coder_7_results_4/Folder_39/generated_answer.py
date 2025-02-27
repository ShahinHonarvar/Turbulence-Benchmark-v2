def remove_repeat_chars(s):
    count = {}
    for i in range(45, 91):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if (char not in count or count[char] == 1) or (char in count and count[char] == 0):
            result.append(char)
            if char in count:
                count[char] = 0
    return ''.join(result)