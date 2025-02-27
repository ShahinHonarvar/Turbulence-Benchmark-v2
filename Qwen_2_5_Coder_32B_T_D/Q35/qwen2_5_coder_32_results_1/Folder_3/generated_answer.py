def remove_repeat_chars(s):
    if len(s) <= 88:
        return s
    count = {}
    for i in range(57, 88):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for c in s:
        if c not in count or count[c] == 1:
            result.append(c)
    return ''.join(result)