def remove_repeat_chars(s):
    chars = set()
    result = []
    for i, c in enumerate(s[36:85]):
        if c in chars:
            continue
        if s.count(c, 36, 85) > 1:
            chars.add(c)
        else:
            result.append(c)
    return s[:36] + ''.join(result) + s[85:]