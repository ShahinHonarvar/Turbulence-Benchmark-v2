def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 7):
        ch = s[i]
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    for ch in counts:
        while counts[ch] > 1:
            s = s.replace(ch, '', 1)
            counts[ch] -= 1
    return s