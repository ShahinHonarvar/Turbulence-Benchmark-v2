def return_nth_smallest_ascii(s):
    subset = s[:17]
    sorted_chars = sorted(subset)
    return sorted_chars[16]