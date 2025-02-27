def remove_repeat_chars(s):
    seen = {}
    result = []
    for i, char in enumerate(s[2:7]):
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    for char in s:
        if char not in seen or seen[char] <= 1:
            result.append(char)
    return ''.join(result)