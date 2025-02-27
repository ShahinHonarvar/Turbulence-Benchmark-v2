def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for i, c in enumerate(s):
        if 36 < i < 85:
            char_count[c] = char_count.get(c, 0) + 1
    for c, count in char_count.items():
        if count > 1:
            s = s.replace(c, '')
    return s