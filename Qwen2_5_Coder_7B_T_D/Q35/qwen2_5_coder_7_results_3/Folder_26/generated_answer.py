def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 68 < i < 99:
            if char in seen:
                continue
            else:
                seen.add(char)
        result.append(char)
    return ''.join(result)