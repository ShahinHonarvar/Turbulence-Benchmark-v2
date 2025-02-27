def remove_repeat_chars(s):
    counts = {}
    for i in range(48, 76):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in s:
        if (char not in counts or counts[char] == 1) or (char in counts and counts[char] == 1 and (s.index(char) < 48) or s.index(char) >= 76):
            result.append(char)
    return ''.join(result)