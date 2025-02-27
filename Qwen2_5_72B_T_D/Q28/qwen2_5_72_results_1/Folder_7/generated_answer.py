def return_nth_smallest_ascii(s):
    subset = s[12:56]
    unique_chars = sorted(set(subset))
    if len(unique_chars) >= 17:
        return unique_chars[16]
    return None