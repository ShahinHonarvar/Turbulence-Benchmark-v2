def remove_repeat_chars(string: str) -> str:
    counts = {}
    for i, c in enumerate(string):
        if i >= 36 and i < 52:
            counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1:
            string = string.replace(c, '')
    return string