def return_nth_smallest_ascii(s):
    window = s[16:87]
    if len(window) < 15:
        return None
    unique_chars = sorted(set(window))
    return unique_chars[14]