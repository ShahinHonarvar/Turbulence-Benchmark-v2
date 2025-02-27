def return_nth_smallest_ascii(s):
    slice_of_string = s[29:34]
    if len(slice_of_string) < 5:
        return ''
    nth_smallest = sorted(slice_of_string)[4]
    return nth_smallest