def return_nth_smallest_ascii(s):
    first_four_chars = sorted(s[:5])
    return first_four_chars[3]