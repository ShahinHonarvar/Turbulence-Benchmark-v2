def remove_repeat_chars(s: str) -> str:
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1 and 62 < ord(c) < 96:
            s = s.replace(c, '')
    return s