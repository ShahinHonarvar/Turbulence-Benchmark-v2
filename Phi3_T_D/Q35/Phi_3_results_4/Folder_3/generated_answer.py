def remove_repeat_chars(s):
    start, end = (57, 87)
    if len(s) < end:
        return s
    seen = {}
    result = []
    for i, char in enumerate(s):
        if start <= i < end:
            if char in seen:
                seen[char] = True
            else:
                seen[char] = False
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)