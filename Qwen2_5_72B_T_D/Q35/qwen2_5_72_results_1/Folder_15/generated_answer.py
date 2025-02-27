def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if i not in range(1, 4) or char not in seen:
            result.append(char)
        seen.add(char)
    return ''.join(result)