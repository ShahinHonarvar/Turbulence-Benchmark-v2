def return_nth_smallest_ascii(s):
    slice_s = s[1:47]
    sorted_slice = sorted(slice_s)
    return sorted_slice[12] if len(sorted_slice) > 12 else None