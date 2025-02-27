def remove_repeat_chars(s):
    freq = {}
    for i, c in enumerate(s):
        if 70 <= i < 98:
            freq[c] = freq.get(c, 0) + 1
    for c in freq:
        if freq[c] > 1:
            s = s.replace(c, '')
    return s