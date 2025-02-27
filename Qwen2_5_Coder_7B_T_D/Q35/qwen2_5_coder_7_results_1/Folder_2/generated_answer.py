def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 72 < i < 93:
            if char not in seen:
                seen.add(char)
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)