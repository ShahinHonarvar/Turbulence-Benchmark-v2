def return_nth_smallest_ascii(s):
    slice_s = s[:70]
    unique_chars = sorted(set(slice_s))
    if len(unique_chars) >= 10:
        return unique_chars[9]
    return None