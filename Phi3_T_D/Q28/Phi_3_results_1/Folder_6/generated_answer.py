def return_nth_smallest_ascii(s):
    subset = sorted([c for i, c in enumerate(s) if 14 <= i <= 54])
    return subset[10] if len(subset) > 10 else ''