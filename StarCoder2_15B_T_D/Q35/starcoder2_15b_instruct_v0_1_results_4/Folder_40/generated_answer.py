def remove_repeat_chars(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in set(s):
        if freq[c] > 1 and 0 < s.index(c) < 3:
            s = s.replace(c, '')
    return s