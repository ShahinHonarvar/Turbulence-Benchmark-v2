def return_nth_smallest_ascii(s):
    subset = s[42:60]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 17:
        return sorted_subset[16]
    else:
        return None