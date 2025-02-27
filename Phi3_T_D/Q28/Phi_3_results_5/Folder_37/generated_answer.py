def return_nth_smallest_ascii(s):
    slice_s = s[28:68]
    unique_chars = sorted(set(slice_s))
    if len(unique_chars) < 15:
        return None
    else:
        return unique_chars[14]