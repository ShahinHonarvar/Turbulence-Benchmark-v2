def return_nth_smallest_ascii(s):
    sliced_string = s[24:72]
    sorted_string = sorted(sliced_string)
    return sorted_string[7]