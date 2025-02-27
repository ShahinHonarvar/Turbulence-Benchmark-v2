def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(0, min(3, len(s))):
        if s[i] not in seen:
            seen.add(s[i])
            result.append(s[i])
    return ''.join(result)