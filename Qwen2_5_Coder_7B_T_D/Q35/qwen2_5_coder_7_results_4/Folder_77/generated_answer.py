def remove_repeat_chars(s):
    counts = {}
    for i in range(356, 988):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in s:
        if (char not in counts or counts[char] == 1) and (s.index(char) < 355 or s.rindex(char) > 987):
            result.append(char)
    return ''.join(result)