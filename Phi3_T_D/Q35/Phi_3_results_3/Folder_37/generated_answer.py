def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s[2:7]):
        if c not in seen and s[2:7].count(c) == 1:
            result.append(c)
        seen.add(c)
    return s[:2] + ''.join(result) + s[7:]