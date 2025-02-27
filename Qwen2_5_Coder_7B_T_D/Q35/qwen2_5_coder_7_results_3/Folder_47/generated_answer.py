def remove_repeat_chars(s):
    seen = set()
    result = list(s)
    for i in range(30, 53):
        if s[i] in seen:
            while s[i] in result:
                result.remove(s[i])
        else:
            seen.add(s[i])
    return ''.join(result)