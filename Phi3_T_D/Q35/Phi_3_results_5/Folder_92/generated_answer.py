def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    seen = set()
    result = []
    for i in range(2):
        char = s[i]
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result) + s[2:]