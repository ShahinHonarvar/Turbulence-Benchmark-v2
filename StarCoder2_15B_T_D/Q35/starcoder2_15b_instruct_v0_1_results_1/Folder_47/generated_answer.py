def remove_repeat_chars(string):
    counts = {}
    for i, c in enumerate(string[29:53]):
        if c not in counts:
            counts[c] = [i]
        else:
            counts[c].append(i)
    for c, indices in counts.items():
        if len(indices) > 1:
            string = ''.join((string[i] for i in range(len(string)) if i not in indices))
    return string