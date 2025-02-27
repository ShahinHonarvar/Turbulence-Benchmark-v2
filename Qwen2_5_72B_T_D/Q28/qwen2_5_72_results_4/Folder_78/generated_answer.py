def return_nth_smallest_ascii(s):
    valid_chars = s[:88]
    sorted_chars = sorted(valid_chars)
    return sorted_chars[13]