def return_nth_smallest_ascii(s):
    subset = s[33:61]
    unique_chars = sorted(set(subset))
    return unique_chars[17] if len(unique_chars) > 17 else None