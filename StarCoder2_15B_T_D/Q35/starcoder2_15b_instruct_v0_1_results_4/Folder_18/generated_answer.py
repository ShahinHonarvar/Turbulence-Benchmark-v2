def remove_repeat_chars(text):
    counts = {}
    for i, c in enumerate(text):
        if c not in counts:
            counts[c] = [i]
        else:
            counts[c].append(i)
    for c, indices in counts.items():
        if len(indices) > 1 and 56 < min(indices) < 90 < max(indices):
            text = text.replace(c, '')
    return text