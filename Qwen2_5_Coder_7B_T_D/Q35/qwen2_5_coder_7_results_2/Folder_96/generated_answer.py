def remove_repeat_chars(s):
    counts = {}
    for i in range(61, 200):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = []
    for char in s:
        if counts[char] == 1 or char not in counts:
            result.append(char)
    return ''.join(result)