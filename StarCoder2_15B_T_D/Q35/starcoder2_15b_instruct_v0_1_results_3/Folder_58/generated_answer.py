def remove_repeat_chars(s: str) -> str:
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    indices = [i for i, c in enumerate(s) if counts[c] > 1 and 103 < i < 802]
    unique_chars = set((s[i] for i in indices))
    return ''.join((c for c in s if c not in unique_chars))