def return_nth_smallest_ascii(s):
    subset = sorted((c for i, c in enumerate(s) if 50 <= i <= 75))
    return subset[6]