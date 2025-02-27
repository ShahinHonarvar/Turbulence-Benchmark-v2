def return_nth_smallest_ascii(s):
    sliced_str = s[4:34]
    sorted_chars = sorted(sliced_str)
    return sorted_chars[3]