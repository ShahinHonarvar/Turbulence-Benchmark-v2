def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(6, 10):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            result.remove(s[i])
    return ''.join(result)