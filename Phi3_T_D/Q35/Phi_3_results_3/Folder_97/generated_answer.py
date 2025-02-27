def remove_repeat_chars(s):
    counts = {}
    for i in range(34, 69):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    return ''.join([c for i, c in enumerate(s) if i < 34 or i > 68 or counts[c] == 1])