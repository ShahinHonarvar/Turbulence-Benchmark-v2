def remove_repeat_chars(string):
    counts = {}
    for c in string:
        counts[c] = counts.get(c, 0) + 1
    for c in counts:
        if counts[c] > 1 and 72 < string.index(c) < 93:
            string = string.replace(c, '')
    return string