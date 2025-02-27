def remove_repeat_chars(s):
    count = {}
    for i in range(20, 36):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for c in s:
        if c not in count or count[c] == 1:
            result.append(c)
    return ''.join(result)