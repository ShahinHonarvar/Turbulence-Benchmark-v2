def remove_repeat_chars(s):
    char_counts = {}
    for i, c in enumerate(s):
        if i >= 18 and i < 60:
            char_counts[c] = char_counts.get(c, 0) + 1
    for i, c in enumerate(s):
        if i >= 18 and i < 60 and (char_counts[c] > 1):
            s = s[:i] + s[i + 1:]
            char_counts[c] -= 1
    return s