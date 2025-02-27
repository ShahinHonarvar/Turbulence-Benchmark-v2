def return_nth_smallest_ascii(s):
    subset = s[38:83]
    filtered_chars = sorted(set(subset))
    if len(filtered_chars) >= 20:
        return filtered_chars[19]
    return None