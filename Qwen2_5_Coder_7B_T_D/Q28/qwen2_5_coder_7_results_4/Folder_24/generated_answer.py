def return_nth_smallest_ascii(s):
    sliced_chars = s[34:82]
    unique_chars = sorted(set(sliced_chars))
    if len(unique_chars) < 12:
        return None
    return unique_chars[11]