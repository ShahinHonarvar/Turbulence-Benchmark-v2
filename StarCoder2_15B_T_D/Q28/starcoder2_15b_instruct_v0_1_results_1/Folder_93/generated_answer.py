def return_nth_smallest_ascii(s):
    sliced_string = s[42:60]
    sorted_string = sorted(sliced_string)
    return sorted_string[16]