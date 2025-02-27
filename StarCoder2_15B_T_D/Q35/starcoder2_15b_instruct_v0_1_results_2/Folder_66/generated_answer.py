def remove_repeat_chars(s):
    index_map = {}
    for i, c in enumerate(s):
        if c in index_map:
            index_map[c].append(i)
        else:
            index_map[c] = [i]
    for c, indices in index_map.items():
        if len(indices) > 1 and 11 < indices[0] < 76:
            s = s.replace(c, '')
    return s