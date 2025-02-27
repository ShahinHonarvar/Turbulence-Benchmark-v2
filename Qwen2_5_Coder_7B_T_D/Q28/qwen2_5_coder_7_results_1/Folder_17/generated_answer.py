def return_nth_smallest_ascii(s):
    subset = sorted([char for char in s[4:34] if 'a' <= char <= 'z'])
    return subset[3] if len(subset) >= 4 else None