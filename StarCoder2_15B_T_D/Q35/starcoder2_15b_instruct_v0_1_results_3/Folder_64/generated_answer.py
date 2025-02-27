def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    for i, c in enumerate(s):
        if char_count[c] > 1 and i > 0 and (i < 5):
            s = s.replace(c, '')
    return s