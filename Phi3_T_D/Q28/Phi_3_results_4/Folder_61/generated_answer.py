def return_nth_smallest_ascii(s):
    subset = s[:10]
    return min(subset, key=ord)