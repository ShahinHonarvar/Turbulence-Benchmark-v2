def return_nth_smallest_ascii(s):
    slice_s = s[58:86]
    sorted_chars = sorted(slice_s)
    nth_smallest = sorted_chars[18]
    return nth_smallest