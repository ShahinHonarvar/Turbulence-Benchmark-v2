def remove_repeat_chars(string):
    counts = {}
    for c in string[70:98]:
        counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1:
            string = string.replace(c, '')
    return string