def return_nth_smallest_ascii(s):
    window = s[24:72]
    sorted_window = sorted(window)
    return sorted_window[7]