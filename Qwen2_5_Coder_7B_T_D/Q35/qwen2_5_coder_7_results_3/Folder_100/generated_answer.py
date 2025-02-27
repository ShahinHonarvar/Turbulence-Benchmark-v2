def remove_repeat_chars(s):
    counts = {}
    for i in range(44, 78):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for i in range(len(s)):
        if (i < 44 or i >= 78) or s[i] not in counts or counts[s[i]] == 1:
            result.append(s[i])
    return ''.join(result)