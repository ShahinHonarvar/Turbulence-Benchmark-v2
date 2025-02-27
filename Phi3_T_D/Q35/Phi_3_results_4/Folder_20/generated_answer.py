def remove_repeat_chars(s):
    indices = range(27, 96)
    seen = set()
    result = []
    for i, char in enumerate(s[27:95]):
        if char not in seen:
            seen.add(char)
        else:
            result.remove(char)
    return ''.join(result)