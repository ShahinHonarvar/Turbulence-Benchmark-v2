def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(2):
        char = s[i]
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)