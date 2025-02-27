def remove_repeat_chars(s):
    target_range = s[73:84]
    seen = set()
    result = []
    for i, c in enumerate(s):
        if i < 73 or i >= 84 or c not in target_range:
            result.append(c)
        elif c not in seen:
            seen.add(c)
            if target_range.count(c) == 1:
                result.append(c)
    return ''.join(result)