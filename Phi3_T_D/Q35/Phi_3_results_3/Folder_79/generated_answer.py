def remove_repeat_chars(s):
    unique_chars = set()
    result = []
    for i in range(1, 7):
        char = s[i]
        if char not in unique_chars:
            unique_chars.add(char)
            result.append(char)
    result.extend(s[:1] + s[7:])
    return ''.join(result)