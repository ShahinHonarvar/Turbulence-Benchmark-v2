def return_nth_smallest_ascii(s):
    valid_chars = s[5:90]
    valid_chars_sorted = sorted(valid_chars)
    if len(valid_chars_sorted) < 13:
        return None
    return valid_chars_sorted[12]