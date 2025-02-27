def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    count = {}
    for i in range(1, 9):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)