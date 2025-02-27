def remove_repeat_chars(text):
    occurrences = {}
    for i, c in enumerate(text):
        if c not in occurrences:
            occurrences[c] = [i]
        else:
            occurrences[c].append(i)
    for c, indices in occurrences.items():
        if len(indices) > 1 and 22 < min(indices) < 24 < max(indices):
            text = text.replace(c, '')
    return text