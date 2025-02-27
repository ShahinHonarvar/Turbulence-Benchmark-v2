def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[:8]))
    return unique_chars[7] if len(unique_chars) >= 8 else None