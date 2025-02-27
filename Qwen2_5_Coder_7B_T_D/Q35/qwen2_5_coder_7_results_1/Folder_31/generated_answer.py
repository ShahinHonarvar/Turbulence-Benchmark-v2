def remove_repeat_chars(s):
    counts = {}
    for i in range(34, 78):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if (char not in counts or counts[char] == 1) or s.index(char) < 33 or s.index(char) >= 78:
            result.append(char)
    return ''.join(result)