def remove_repeat_chars(s):
    counts = {}
    for i in range(10, 76):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if (char not in counts or counts[char] == 1) or (char in counts and counts[char] == 1 if s.index(char) < 10 or s.rindex(char) > 76 else True):
            result.append(char)
    return ''.join(result)