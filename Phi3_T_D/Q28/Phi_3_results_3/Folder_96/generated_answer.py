def return_nth_smallest_ascii(s):
    first_18_chars = sorted(s[:18])
    return first_18_chars[17]