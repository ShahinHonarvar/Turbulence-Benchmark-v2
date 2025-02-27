def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(90, 200):
        if len(s) > i and s[i] in seen:
            continue
        else:
            seen.add(s[i])
            result.append(s[i])
    return ''.join(result)