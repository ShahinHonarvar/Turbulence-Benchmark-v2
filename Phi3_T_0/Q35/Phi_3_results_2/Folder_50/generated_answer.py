def remove_repeat_chars(s):
    start, end = (13, 76)
    seen = set()
    result = []
    for i, char in enumerate(s):
        if start <= i < end:
            if char in seen:
                continue
            seen.add(char)
        result.append(char)
    return ''.join(result)