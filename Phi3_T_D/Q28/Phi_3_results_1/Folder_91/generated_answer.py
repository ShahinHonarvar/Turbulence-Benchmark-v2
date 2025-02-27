def return_nth_smallest_ascii(s):
    mapped = sorted(((ord(c), c) for c in s[:8]))
    return mapped[7][1] if mapped[7][0] else None