def remove_repeat_chars(s):
    counts = {}
    for i in range(50, 74):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''
    for char in s:
        if (char not in counts or counts[char] == 1) and (s.index(char) < 50 or s.rindex(char) > 74):
            result += char
    return result