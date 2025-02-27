def remove_repeat_chars(s):
    start, end = (56, 90)
    seen = set()
    result = []
    for i in range(start, end):
        char = s[i]
        if char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)