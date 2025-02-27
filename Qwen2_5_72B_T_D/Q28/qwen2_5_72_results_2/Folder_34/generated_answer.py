def return_nth_smallest_ascii(s):
    sub_str = s[:19]
    sorted_chars = sorted(sub_str)
    return sorted_chars[18]