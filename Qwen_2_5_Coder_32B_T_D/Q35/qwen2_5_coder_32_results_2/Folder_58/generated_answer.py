def remove_repeat_chars(s):
    if len(s) <= 803:
        return s
    count = {}
    for i in range(104, 802):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if count.get(char, 0) <= 1 or s.index(char) < 104 or s.index(char) >= 802:
            result.append(char)
    return ''.join(result)