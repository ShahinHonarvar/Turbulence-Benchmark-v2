def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(1, 6):
        c = s[i]
        if c not in seen:
            result.append(c)
            seen.add(c)
    return ''.join(result)