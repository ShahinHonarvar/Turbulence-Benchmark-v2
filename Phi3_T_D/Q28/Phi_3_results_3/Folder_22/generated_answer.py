def return_nth_smallest_ascii(s):
    unique_chars = set(s[:17])
    return min(unique_chars, key=ord)