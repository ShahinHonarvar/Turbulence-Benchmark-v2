def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    count = {}
    for i in range(61, 200):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if not (60 < s.index(char) < 200 and count[char] > 1):
            result.append(char)
    return ''.join(result)