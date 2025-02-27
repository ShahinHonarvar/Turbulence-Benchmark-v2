def return_nth_smallest_ascii(s):
    subset = s[50:60]
    return sorted(subset, key=ord)[4]