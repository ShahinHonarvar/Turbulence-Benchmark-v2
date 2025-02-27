def remove_repeat_chars(string):
    counts = {}
    indices = {}
    for i, c in enumerate(string):
        counts[c] = counts.get(c, 0) + 1
        indices[c] = indices.get(c, []) + [i]
    for c, count in counts.items():
        if count > 1 and 16 < indices[c][0] < 87:
            string = string.replace(c, '')
    return string