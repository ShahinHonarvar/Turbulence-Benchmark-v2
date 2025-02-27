def return_nth_smallest_ascii(s):
    subset = s[51:79]
    unique_chars = sorted(set(subset))
    if len(unique_chars) >= 9:
        return unique_chars[8]
    return None