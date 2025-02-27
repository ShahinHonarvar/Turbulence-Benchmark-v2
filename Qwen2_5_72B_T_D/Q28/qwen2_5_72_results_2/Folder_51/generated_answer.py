def return_nth_smallest_ascii(s):
    subset = s[10:74]
    sorted_subset = sorted(subset)
    return sorted_subset[8] if len(sorted_subset) > 8 else None