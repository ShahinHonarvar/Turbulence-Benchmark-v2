def remove_repeat_chars(text):
    indices = {}
    for i, c in enumerate(text):
        if c not in indices:
            indices[c] = []
        indices[c].append(i)
    for c, c_indices in indices.items():
        if len(c_indices) > 1 and all((72 < i < 93 for i in c_indices)):
            text = text.replace(c, '')
    return text