def remove_repeat_chars(s: str) -> str:
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c, count in freq.items():
        if count > 1 and 34 < s.index(c) < 69:
            s = s.replace(c, '')
    return s