def return_nth_smallest_ascii(s):
    filtered_chars = sorted([c for i, c in enumerate(s) if 32 <= i <= 67])
    if len(filtered_chars) < 12:
        return None
    return filtered_chars[11]