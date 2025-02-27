def return_nth_smallest_ascii(s):
    subset = s[:88]
    sorted_chars = sorted(subset)
    return sorted_chars[13]