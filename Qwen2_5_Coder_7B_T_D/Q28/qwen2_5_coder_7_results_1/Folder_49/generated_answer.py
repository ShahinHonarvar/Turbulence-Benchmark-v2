def return_nth_smallest_ascii(s):
    subset = sorted((char for char in s[20:81] if char in s))
    if len(subset) < 11:
        return None
    return subset[10]