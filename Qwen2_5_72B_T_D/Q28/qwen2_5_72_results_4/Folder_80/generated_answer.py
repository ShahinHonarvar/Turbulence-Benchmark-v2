def return_nth_smallest_ascii(s):
    subset = s[51:90]
    subset = sorted(set(subset))
    if len(subset) < 14:
        return None
    return subset[13]