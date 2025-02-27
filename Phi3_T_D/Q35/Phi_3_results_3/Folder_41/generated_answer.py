def remove_repeat_chars(s):
    seen, result = (set(), [])
    for i, c in enumerate(s):
        if 3 < i < 8 and c in seen:
            continue
        seen.add(c)
        result.append(c)
    return ''.join(result)