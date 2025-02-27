def return_nth_smallest_ascii(s):
    subset = sorted(set(s[20:31]))
    return subset[7] if len(subset) >= 8 else None