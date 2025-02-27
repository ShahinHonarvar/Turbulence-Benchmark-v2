def return_nth_smallest_ascii(s):
    subset = s[24:89]
    unique_chars = sorted(set(subset))
    return unique_chars[10]