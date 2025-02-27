def remove_repeat_chars(text):
    occurrences = {}
    for i, c in enumerate(text):
        if 42 < i < 87:
            occurrences[c] = occurrences.get(c, []) + [i]
    for c, indices in occurrences.items():
        if len(indices) > 1:
            text = ''.join((text[i] for i in range(len(text)) if i not in indices))
    return text