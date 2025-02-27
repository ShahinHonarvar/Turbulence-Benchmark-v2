def return_nth_smallest_ascii(s):
    subset = s[38:83]
    sorted_chars = sorted(set(subset))
    if len(sorted_chars) < 20:
        return None
    return sorted_chars[19]