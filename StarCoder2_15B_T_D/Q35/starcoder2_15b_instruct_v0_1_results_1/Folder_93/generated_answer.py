def remove_repeat_chars(s: str) -> str:
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    indices = {}
    for i, c in enumerate(s):
        if counts[c] > 1 and 57 < i < 85:
            indices[c] = indices.get(c, []) + [i]
    for c, idx_list in indices.items():
        for idx in sorted(idx_list, reverse=True):
            s = s[:idx] + s[idx + 1:]
    return s