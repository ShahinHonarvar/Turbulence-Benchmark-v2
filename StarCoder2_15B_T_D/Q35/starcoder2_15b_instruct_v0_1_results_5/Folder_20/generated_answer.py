def remove_repeat_chars(s):
    seen = {}
    for i, c in enumerate(s):
        if 27 < i < 96 and c in seen:
            s = s.replace(c, '')
        else:
            seen[c] = i
    return s