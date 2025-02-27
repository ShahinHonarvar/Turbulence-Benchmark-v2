def remove_repeat_chars(s):
    seen = set()
    result = []
    for index in range(6):
        char = s[index]
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)