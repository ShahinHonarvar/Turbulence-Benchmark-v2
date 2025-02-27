def remove_repeat_chars(string):
    seen = {}
    result = []
    for i, c in enumerate(string):
        if c not in seen:
            seen[c] = i
            result.append(c)
    return ''.join(result)