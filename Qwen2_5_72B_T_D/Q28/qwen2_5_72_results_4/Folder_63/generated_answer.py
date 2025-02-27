def return_nth_smallest_ascii(s):
    subset = [s[i] for i in range(47, 71) if i < len(s)]
    sorted_subset = sorted(subset)
    return sorted_subset[13] if len(sorted_subset) > 13 else None