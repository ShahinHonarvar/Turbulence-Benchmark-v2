def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[:9]))
    return unique_chars[8] if len(unique_chars) >= 9 else None