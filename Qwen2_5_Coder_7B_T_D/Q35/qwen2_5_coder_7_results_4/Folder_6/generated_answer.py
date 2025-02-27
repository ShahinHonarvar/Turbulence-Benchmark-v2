def remove_repeat_chars(s):
    counts = {}
    for i in range(20, 93):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if counts[char] == 1 or char not in range(20, 93):
            result.append(char)
    return ''.join(result)