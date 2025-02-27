def return_nth_smallest_ascii(s):
    window = s[5:11]
    sorted_window = sorted(window)
    return sorted_window[5] if len(sorted_window) >= 6 else None