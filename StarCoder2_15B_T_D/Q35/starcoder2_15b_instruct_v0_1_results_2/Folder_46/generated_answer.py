def remove_repeat_chars(s):
    freq = {}
    for c in s[10:79]:
        freq[c] = freq.get(c, 0) + 1
    for c in freq:
        if freq[c] > 1:
            s = s.replace(c, '')
    return s