def remove_repeat_chars(s):
    seen = {}
    result = []
    for i, char in enumerate(s):
        if 19 < i < 32:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        else:
            result.append(char)
    for i, char in enumerate(result):
        if 19 < i < 32 and seen[char] > 1:
            seen[char] -= 1
        else:
            result[i] = char
    return ''.join(result)