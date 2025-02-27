def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    count = {}
    for i in range(14, 76):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if count.get(char, 0) <= 1 or (count[char] > 1 and char not in s[14:76]):
            result.append(char)
    return ''.join(result)