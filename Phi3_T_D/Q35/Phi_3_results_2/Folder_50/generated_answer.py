def remove_repeat_chars(s):
    seen, modified = (set(), '')
    for i, c in enumerate(s[13:75]):
        if c not in seen:
            seen.add(c)
            modified += c
        elif i not in range(13, 76):
            modified += c
    return s[:13] + modified + s[76:]