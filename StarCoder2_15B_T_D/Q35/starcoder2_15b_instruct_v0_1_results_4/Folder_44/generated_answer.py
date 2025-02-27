def remove_repeat_chars(string):
    counts = {}
    for i, c in enumerate(string):
        if c not in counts:
            counts[c] = [i]
        else:
            counts[c].append(i)
    for c, indices in counts.items():
        if len(indices) > 1 and 36 < indices[0] < 52:
            string = string.replace(c, '')
    return string