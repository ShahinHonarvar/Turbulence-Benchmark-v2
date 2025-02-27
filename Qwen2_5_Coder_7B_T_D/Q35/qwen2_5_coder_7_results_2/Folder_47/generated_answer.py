def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 29 < i < 53:
            if char in seen:
                continue
            seen.add(char)
        result.append(char)
    return ''.join(result)