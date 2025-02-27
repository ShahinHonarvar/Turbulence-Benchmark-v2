def remove_repeat_chars(string):
    counts = {}
    for i, c in enumerate(string):
        if i >= 30 and i < 200:
            counts[c] = counts.get(c, 0) + 1
    for c in counts:
        if counts[c] > 1:
            string = string.replace(c, '')
    return string