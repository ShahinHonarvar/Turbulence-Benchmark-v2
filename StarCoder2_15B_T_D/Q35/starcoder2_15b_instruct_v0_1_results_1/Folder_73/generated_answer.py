def remove_repeat_chars(s: str) -> str:
    counter = {}
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    for c in set(s):
        if counter[c] > 1 and 10 < s.index(c) < 76:
            s = s.replace(c, '')
    return s