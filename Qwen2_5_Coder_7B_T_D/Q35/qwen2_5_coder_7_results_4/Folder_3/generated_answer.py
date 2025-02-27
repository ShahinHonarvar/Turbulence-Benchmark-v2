def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 56 < i < 88:
            if char in seen:
                continue
            seen.add(char)
        result.append(char)
    return ''.join(result)