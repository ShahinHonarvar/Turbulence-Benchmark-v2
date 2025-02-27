def remove_repeat_chars(s):
    if len(s) <= 53:
        return s
    count = {}
    for i in range(30, 53):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if count.get(char, 0) <= 1 or s.index(char) < 30 or s.index(char) > 52:
            result.append(char)
    return ''.join(result)