def remove_repeat_chars(s):
    start, end = (16, 87)
    seen = set()
    result = []
    for i in range(start, end):
        char = s[i]
        if char not in seen and s[start:end].count(char) > 1:
            seen.add(char)
            result.append(char)
    return ''.join(result)