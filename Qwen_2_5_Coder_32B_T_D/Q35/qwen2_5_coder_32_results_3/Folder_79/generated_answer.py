def remove_repeat_chars(s):
    count = {}
    for i in range(2, 7):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if not (2 <= s.index(char) <= 6 and count.get(char, 0) > 1):
            result.append(char)
    return ''.join(result)