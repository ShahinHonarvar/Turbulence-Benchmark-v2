def remove_repeat_chars(s):
    check = set()
    result = []
    for i, c in enumerate(s):
        if 13 < i < 70:
            if c in check:
                continue
            check.add(c)
        result.append(c)
    return ''.join(result)