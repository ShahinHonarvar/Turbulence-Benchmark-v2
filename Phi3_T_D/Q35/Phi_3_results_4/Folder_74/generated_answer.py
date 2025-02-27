def remove_repeat_chars(s):
    target_chars = set(s[69:97] if len(s) > 96 else [])
    result = []
    for c in s:
        if c not in target_chars or result.count(c) < 1:
            result.append(c)
    return ''.join(result)