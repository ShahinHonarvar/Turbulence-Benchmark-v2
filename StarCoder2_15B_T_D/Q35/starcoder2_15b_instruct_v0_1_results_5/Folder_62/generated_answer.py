def remove_repeat_chars(s: str) -> str:
    char_count = dict()
    for i, c in enumerate(s):
        if i >= 50 and i < 92:
            char_count[c] = char_count.get(c, 0) + 1
    for c in char_count:
        if char_count[c] > 1:
            s = s.replace(c, '')
    return s