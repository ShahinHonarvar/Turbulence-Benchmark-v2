def return_nth_smallest_ascii(s):
    subset = s[36:80]
    filtered_chars = sorted(set(subset))
    if len(filtered_chars) < 12:
        return None
    return filtered_chars[11]