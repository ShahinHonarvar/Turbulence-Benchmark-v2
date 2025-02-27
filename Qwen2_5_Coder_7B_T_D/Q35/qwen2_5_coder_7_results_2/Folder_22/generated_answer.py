def remove_repeat_chars(s):
    count = {}
    for i in range(50, 200):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if (s[i] not in count or count[s[i]] == 1) and (i < 50 or i >= 200):
            result += s[i]
    return result