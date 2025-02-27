def remove_repeat_chars(s: str) -> str:
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in count:
        if count[c] > 1 and 19 < s.index(c) < 32:
            s = s.replace(c, '')
    return s