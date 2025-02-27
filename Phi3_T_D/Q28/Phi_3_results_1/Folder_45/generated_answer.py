def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[:16]))
    return unique_chars[15] if len(unique_chars) >= 16 else None