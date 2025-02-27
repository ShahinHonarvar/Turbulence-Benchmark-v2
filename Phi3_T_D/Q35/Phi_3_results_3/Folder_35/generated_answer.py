def remove_repeat_chars(s):
    seen = set()
    start, end = (77, 84)
    new_s = s[:start]
    for i in range(start, end):
        if s[i] not in seen:
            new_s += s[i]
            seen.add(s[i])
    new_s += s[end:]
    return new_s