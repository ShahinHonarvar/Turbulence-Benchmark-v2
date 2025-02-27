def return_nth_smallest_ascii(s):
    within_range = s[51:79]
    ascii_values = sorted(set(within_range))
    return ascii_values[8]