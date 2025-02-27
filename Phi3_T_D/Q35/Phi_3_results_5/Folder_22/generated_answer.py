def remove_repeat_chars(s):
    start, end = (50, 200)
    seen = set()
    for i in range(start, end):
        if s[i] in seen:
            s = s.replace(s[i], '', 1)
        else:
            seen.add(s[i])
    return s