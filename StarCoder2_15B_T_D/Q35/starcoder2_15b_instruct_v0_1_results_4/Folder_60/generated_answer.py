def remove_repeat_chars(s):
    freq = {}
    for c in s[38:52]:
        freq[c] = freq.get(c, 0) + 1
    return ''.join([c for c in s if freq[c] == 1])