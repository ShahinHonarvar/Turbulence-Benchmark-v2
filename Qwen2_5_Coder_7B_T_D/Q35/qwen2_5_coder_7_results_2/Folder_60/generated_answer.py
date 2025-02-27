def remove_repeat_chars(s):
    counts = {}
    for i in range(38, 52):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if (char not in counts or counts[char] == 1) and (i < 38 or i >= 52 or char not in set(s[38:52])):
            result.append(char)
    return ''.join(result)