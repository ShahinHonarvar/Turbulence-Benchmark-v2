def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s[90:200]):
        if c not in seen:
            seen.add(c)
            result.append(c)
        if i == len(s[90:200]) - 1:
            result.extend(s[:90] + s[200:])
    return ''.join(result)