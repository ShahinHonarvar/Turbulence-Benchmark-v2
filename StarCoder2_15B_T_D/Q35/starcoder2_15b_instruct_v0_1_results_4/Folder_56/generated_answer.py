def remove_repeat_chars(s: str) -> str:
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c in set(s):
        if counts[c] > 1 and 7 < s.index(c) < 9:
            s = s.replace(c, '')
    return s