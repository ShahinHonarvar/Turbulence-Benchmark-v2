def remove_repeat_chars(s: str) -> str:
    counts = {}
    for i, c in enumerate(s):
        if i >= 103 and i < 802:
            counts[c] = counts.get(c, 0) + 1
    for c in counts:
        if counts[c] > 1:
            s = s.replace(c, '')
    return s