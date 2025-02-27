def return_nth_smallest_ascii(s):
    range_slice = s[48:77]
    sorted_slice = sorted(range_slice)
    return sorted_slice[4]