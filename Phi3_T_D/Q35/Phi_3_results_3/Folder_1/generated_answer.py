def remove_repeat_chars(s):
    i, j = (18, 87)
    seen = set()
    result = []
    while i <= j:
        char = s[i]
        if char not in seen:
            seen.add(char)
            result.append(char)
        i += 1
    return ''.join(result)