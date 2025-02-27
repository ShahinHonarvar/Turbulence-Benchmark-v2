def return_nth_smallest_ascii(s):
    subset = s[33:86]
    sorted_chars = sorted(subset)
    return sorted_chars[12]