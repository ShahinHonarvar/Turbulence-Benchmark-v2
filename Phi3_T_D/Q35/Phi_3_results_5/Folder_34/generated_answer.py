def remove_repeat_chars(s):
    seen = {}
    result = []
    for i, c in enumerate(s):
        if 70 < i < 200 and c in seen:
            seen[c] = True
        elif c not in seen:
            seen[c] = False
            result.append(c)
    return ''.join(result)