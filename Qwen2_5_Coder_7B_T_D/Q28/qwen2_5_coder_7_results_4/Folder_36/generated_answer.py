def return_nth_smallest_ascii(s):
    subset = s[17:57]
    sorted_subset = sorted(set(subset))
    return sorted_subset[8]