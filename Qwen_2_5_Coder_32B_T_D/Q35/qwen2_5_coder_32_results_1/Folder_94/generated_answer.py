def remove_repeat_chars(s):
    if len(s) <= 87:
        return s
    count = {}
    for i in range(43, 87):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if count.get(char, 0) > 1:
            continue
        result.append(char)
    return ''.join(result)