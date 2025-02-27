def remove_repeat_chars(s):
    seen = set()
    result = list(s)
    for i in range(100, 200):
        if s[i] in seen:
            result[i] = ''
        else:
            seen.add(s[i])
    return ''.join(result)