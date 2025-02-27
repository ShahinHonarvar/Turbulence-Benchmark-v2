def return_nth_smallest_ascii(s):
    subset = s[:88]
    sorted_subset = sorted(subset)
    return sorted_subset[13]