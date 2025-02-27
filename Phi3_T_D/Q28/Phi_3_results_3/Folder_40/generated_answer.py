def return_nth_smallest_ascii(s):
    first_five_chars = sorted(s[:5])
    return first_five_chars[4]