def remove_repeat_chars(s):
    counts = {}
    for i in range(58, 84):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for i, char in enumerate(s):
        if 57 < i < 84 and counts[char] > 1 or (57 >= i or i >= 84):
            result.append(char)
    return ''.join(result)