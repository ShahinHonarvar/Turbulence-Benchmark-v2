def remove_repeat_chars(s):
    if len(s) < 151:
        return s
    seen = set()
    result = []
    for i in range(50, 200):
        char = s[i]
        if char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)