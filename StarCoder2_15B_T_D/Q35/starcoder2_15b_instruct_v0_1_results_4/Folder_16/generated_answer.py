def remove_repeat_chars(s):
    char_indices = {}
    for i, c in enumerate(s):
        if c in char_indices:
            char_indices[c].append(i)
        else:
            char_indices[c] = [i]
    for c, indices in char_indices.items():
        if len(indices) > 1 and 90 < indices[0] < 97:
            s = s.replace(c, '')
    return s