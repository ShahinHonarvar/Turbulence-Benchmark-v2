def remove_repeat_chars(string):
    counts = {}
    for i, c in enumerate(string):
        if i >= 51 and i < 76:
            counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1:
            string = string.replace(c, '')
    return string