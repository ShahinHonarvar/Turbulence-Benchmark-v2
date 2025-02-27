def remove_repeat_chars(s):
    freq = {}
    for c in s[86:90]:
        freq[c] = freq.get(c, 0) + 1
    for c in freq:
        if freq[c] > 1:
            s = s.replace(c, '')
    return s