def remove_repeat_chars(s):
    seen = {}
    result = []
    for i, char in enumerate(s):
        if 36 < i < 52:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        else:
            seen[char] = 0
    for char in s:
        if seen[char] == 0:
            result.append(char)
    return ''.join(result)