def remove_repeat_chars(s):
    indices = range(27, 96)
    seen = {}
    result = []
    for i, char in enumerate(s):
        if i in indices and char in seen:
            seen[char] += 1
        elif i in indices:
            seen[char] = 1
    for i, char in enumerate(s):
        if i not in indices or seen[char] == 1:
            result.append(char)
    return ''.join(result)