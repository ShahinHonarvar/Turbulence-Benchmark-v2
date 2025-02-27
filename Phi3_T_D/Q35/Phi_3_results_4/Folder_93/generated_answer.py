def remove_repeat_chars(s):
    start, end = (58, 84)
    seen = set()
    result = []
    for index, char in enumerate(s):
        if start <= index < end:
            if char in seen:
                continue
            seen.add(char)
            result.append(char)
        else:
            result.append(char)
    return ''.join(result)