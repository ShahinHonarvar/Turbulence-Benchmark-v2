def remove_repeat_chars(s):
    freq = {}
    for c in s[70:200]:
        freq[c] = freq.get(c, 0) + 1
    for c, count in freq.items():
        if count > 1:
            s = s.replace(c, '')
    return s