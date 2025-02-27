def return_nth_smallest_ascii(s):
    first_four_chars = sorted(s[:4], key=ord)
    return first_four_chars[3]