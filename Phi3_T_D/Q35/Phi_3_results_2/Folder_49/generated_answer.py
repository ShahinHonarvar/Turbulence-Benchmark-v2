def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(90, 200):
        char = s[i]
        if char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)