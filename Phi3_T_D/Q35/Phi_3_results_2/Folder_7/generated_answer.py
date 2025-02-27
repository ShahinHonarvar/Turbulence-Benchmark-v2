def remove_repeat_chars(s):
    counted_chars = {}
    for i, c in enumerate(s[375:925]):
        counted_chars[c] = counted_chars.get(c, 0) + 1
    result = []
    for i, c in enumerate(s):
        if counted_chars.get(c, 0) > 1 and 375 <= i + 375 < 925:
            continue
        result.append(c)
    return ''.join(result)