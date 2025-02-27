def remove_repeat_chars(s):
    counts = {}
    for i in range(20, 51):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if (char not in counts or counts[char] == 1) and (s.index(char) < 20 or s.rindex(char) > 51):
            result.append(char)
    return ''.join(result)